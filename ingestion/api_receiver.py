from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Dict
from pydantic import BaseModel
from search.query_engine import search_logs

from parser.normalizer import normalize_log
from db.db import get_db
from db.crud import save_log_event
from search.indexers import index_log

router = APIRouter()

class RawLog(BaseModel):
    source: str
    log_data: Dict

@router.get("/search")
async def search_log(query: str = Query(..., description="Search String")):
    res = search_log(query)
    return {
        "hits": res
    }

@router.post("/ingest")
async def ingest_log(log: RawLog, db: AsyncSession = Depends(get_db)):
    try:
        # Step 1: Normalize the raw log
        normalized_log = normalize_log(log.source, log.log_data)

        # Step 2: Add source info before saving/indexing
        full_log = {**normalized_log, "source": log.source}

        # Step 3: Save to database
        saved_log = await save_log_event(db, full_log)

        # Step 4: Index in OpenSearch
        await index_log(full_log)  # Now async-compatible

        return {"status": "success", "id": saved_log.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
