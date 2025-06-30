from fastapi import FastAPI
from alerting.schedular import start_scheduler
from ingestion.api_receiver import router as ingestion_router
from dashboard.routes import router as dashboard_router
from fastapi import APIRouter, Depends
from auth.auth import create_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from auth.users import User
from db.db import get_db
from passlib.hash import bcrypt


app = FastAPI(title = "SEM Log Ingestion API")

@app.on_event("startup")
async def startup_event():
    start_scheduler()


app.include_router(ingestion_router, prefix = "/logs")
app.include_router(dashboard_router, prefix="/dashboard")