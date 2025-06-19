import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db.crud import get_recent_logs
from alerting.rule_engine import load_rules, match_rules
from alerting.notifiers.email import send_email
from alerting.notifiers.slack import send_slack

scheduler = AsyncIOScheduler()

async def alert_check():
    rules = load_rules()
    recent_logs = await get_recent_logs(minutes = 2) # Retain the lead from last 2 mins
    for log in recent_logs:
        for rule in rules:
            if match_rules(log, rule):
                alert = rule["alert"]
                if alert["type"] == "email":
                    await send_email(alert["to"], rule["name"], log)
                elif alert["type"] == "slack":
                    await send_slack(alert["channel"], rule["name"], log)

def start_scheduler():
    scheduler.add_job(alert_check, "interval", minutes = 1)
    scheduler.start()