#pragma once
#include "dq_compute_actor_sources.h"
#include "dq_compute_actor_async_output.h"

#include <ydb/library/yql/dq/actors/protos/dq_events.pb.h>
#include <ydb/library/yql/dq/common/dq_common.h>

#include <ydb/library/yql/minikql/computation/mkql_computation_node_holders.h>
#include <ydb/library/yql/utils/yql_panic.h>

#include <type_traits>

namespace NYql::NDq {

template <class T>
concept TCastsToSourceActorPair =
    std::is_convertible_v<T, std::pair<IDqSourceActor*, NActors::IActor*>>;

template <class T, class TProto>
concept TSourceActorCreatorFunc = requires(T f, TProto&& settings, IDqSourceActorFactory::TArguments args) {
    { f(std::move(settings), std::move(args)) } -> TCastsToSourceActorPair;
};

class TDqSourceFactory : public IDqSourceActorFactory {
public:
    using TCreatorFunction = std::function<std::pair<IDqSourceActor*, NActors::IActor*>(TArguments&& args)>;

    std::pair<IDqSourceActor*, NActors::IActor*> CreateDqSourceActor(TArguments&& args) const override;

    void Register(const TString& type, TCreatorFunction creator);

    template <class TProtoMsg, TSourceActorCreatorFunc<TProtoMsg> TCreatorFunc>
    void Register(const TString& type, TCreatorFunc creator) {
        Register(type,
            [creator = std::move(creator), type](TArguments&& args)
            {
                const google::protobuf::Any& settingsAny = args.InputDesc.GetSource().GetSettings();
                YQL_ENSURE(settingsAny.Is<TProtoMsg>(),
                    "Source \"" << type << "\" settings are expected to have protobuf type " << TProtoMsg::descriptor()->full_name()
                    << ", but got " << settingsAny.type_url());
                TProtoMsg settings;
                YQL_ENSURE(settingsAny.UnpackTo(&settings), "Failed to unpack settings of type \"" << type << "\"");
                return creator(std::move(settings), std::move(args));
        });
    }

private:
    THashMap<TString, TCreatorFunction> CreatorsByType;
};

template <class T>
concept TCastsToSinkPair =
    std::is_convertible_v<T, std::pair<IDqComputeActorAsyncOutput*, NActors::IActor*>>;

template <class T, class TProto>
concept TSinkCreatorFunc = requires(T f, TProto&& settings, IDqSinkFactory::TArguments&& args) {
    { f(std::move(settings), std::move(args)) } -> TCastsToSinkPair;
};

class TDqSinkFactory : public IDqSinkFactory {
public:
    using TCreatorFunction = std::function<std::pair<IDqComputeActorAsyncOutput*, NActors::IActor*>(TArguments&& args)>;

    std::pair<IDqComputeActorAsyncOutput*, NActors::IActor*> CreateDqSink(TArguments&& args) const override;

    void Register(const TString& type, TCreatorFunction creator);

    template <class TProtoMsg, TSinkCreatorFunc<TProtoMsg> TCreatorFunc>
    void Register(const TString& type, TCreatorFunc creator) {
        Register(type,
            [creator = std::move(creator), type](TArguments&& args)
            {
                const google::protobuf::Any& settingsAny = args.OutputDesc.GetSink().GetSettings();
                YQL_ENSURE(settingsAny.Is<TProtoMsg>(),
                    "Sink \"" << type << "\" settings are expected to have protobuf type " << TProtoMsg::descriptor()->full_name()
                    << ", but got " << settingsAny.type_url());
                TProtoMsg settings;
                YQL_ENSURE(settingsAny.UnpackTo(&settings), "Failed to unpack settings of type \"" << type << "\"");
                return creator(std::move(settings), std::move(args));
        });
    }

private:
    THashMap<TString, TCreatorFunction> CreatorsByType;
};

} // namespace NYql::NDq
