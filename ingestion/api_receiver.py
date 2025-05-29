from fastapi import APIRouter, Request, HTTPException
from parser.normalizer import normalize_log
from pydantic import BaseModel
from typing import Dict

router = APIRouter()

class RawLog(BaseModel):
    source: str
    log_data: Dict
    
@router.post("/ingest")
async def ingest_log(log: RawLog):
    try:
        normalize_log = normalize_log(log.source, log.log_data)
        return {"status" : "success", "normalized" : normalize_log}
    except Exception as e:
        raise HTTPException(status_code = 400, detail = str(e))