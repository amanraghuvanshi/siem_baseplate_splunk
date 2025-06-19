from sqlalchemy.ext.asyncio import AsyncSession
from db.models.log_events import LogEvent
from sqlalchemy.future import select
from datetime import datetime, timedelta


async def save_log_events(db: AsyncSession, log_data: dict):
    db_log = LogEvent(**log_data)
    db.add(db_log)
    await db.commit()
    await db.refresh()
    return db_log

async def get_recent_logs(minutes = 2):
    from db.db import AsyncSessionLocal
    now = datetime.utcnow()
    cutoff = now - timedelta(minutes = minutes)
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(LogEvent).where(LogEvent.timestamp >= cutoff)
        )
        return [row._asdict() for row in result.fetchall()]