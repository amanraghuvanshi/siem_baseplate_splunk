import httpx

async def send_slack(channel, subject, log):
    webhook_url = "https://hooks.slack.com/services/xxx/yyy/zzz" # replace with orignial one
    payloads = {
        "text" : f"Warning: *SIEM ALERT:* `{subject}`\n```{log}```"
    }
    
    async with httpx.AsyncClient() as client:
        await client.post(webhook_url, json = payloads)