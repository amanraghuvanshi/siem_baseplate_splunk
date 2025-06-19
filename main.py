from fastapi import FastAPI
from alerting.schedular import start_scheduler
from ingestion.api_receiver import router as ingestion_router
from ux.routes import router as dashboard_router




@app.on_event("startup")
async def startup_event():
    start_scheduler()
app = FastAPI(title = "SEM Log Ingestion API")

app.include_router(ingestion_router, prefix = "/logs")
app.include_router(dashboard_router, prefix="/dashboard")