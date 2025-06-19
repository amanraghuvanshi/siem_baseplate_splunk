from fastapi import APIRouter
from ux.visualizer import get_log_summary, get_severity_chart

router = APIRouter()

@router.get("/summary")
async def log_summary():
    return await get_log_summary()

@router.get("/severity-distribution")
async def severity_distribution():
    return await get_severity_chart()