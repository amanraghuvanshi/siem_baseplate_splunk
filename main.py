from fastapi import FastAPI
from ingestion.api_receiver import router as ingestion_router

app = FastAPI(title = "SEM Log Ingestion API")

app.include_router(ingestion_router, prefix = "/logs")