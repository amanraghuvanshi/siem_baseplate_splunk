from sqlalchemy import func
from db.db import AsyncSessionLocal
from sqlalchemy.future import select
from db.models.log_events import LogEvent

async def get_log_summary():
    async with AsyncSessionLocal() as session:
        count_smt = await session.execute(select(func.count()).select_from(LogEvent))
        total_logs = count_smt.scalar()
        
        severity_stmt = await session.execute(
            select(LogEvent.severity, func.count()).group_by(LogEvent.severity)
        )
        
        severity_count = [{
            "severity" : s,
            "count" : c
        }for s, c in severity_stmt.fetchall()]
        
        return {
            "total_logs": total_logs,
            "by_severity": severity_count
        }

async def get_severity_chart():
    async with AsyncSessionLocal() as sess:
        stmt = await sess.execute(
            select(LogEvent.severity, func.count()).group_by(LogEvent.severity)
        )
        
        data = [{"label": s or "unknown", "value":c } for s, c in stmt.fetchall()]
        
        return data