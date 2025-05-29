from sqlalchemy.ext.asyncio import AsyncSession
from db.models.log_events import LogEvent
from sqlalchemy.future import select


async def save_log_events(db: AsyncSession, log_data: dict):
    db_log = LogEvent(**log_data)
    db.add(db_log)
    await db.commit()
    await db.refresh()
    return db_log