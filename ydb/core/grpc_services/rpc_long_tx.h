#pragma once

#include <ydb/core/tx/scheme_cache/scheme_cache.h>
#include <ydb/core/formats/arrow_helpers.h>

namespace NKikimr::NGRpcService {

TActorId DoLongTxWriteSameMailbox(const TActorContext& ctx, const TActorId& replyTo,
    const NLongTxService::TLongTxId& longTxId, const TString& dedupId,
    const TString& databaseName, const TString& path, const NSchemeCache::TSchemeCacheNavigate& navigateResult,
    std::shared_ptr<arrow::RecordBatch> batch, NYql::TIssues& issues);

}
