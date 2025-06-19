import aiosmtplib
from email.message import EmailMessage

async def send_mail(to_mail, subject, log):
    msg = EmailMessage()
    msg["from"] = "noreply@siem.local"
    msg["to"] = to_mail
    msg["Subject"] = f"SIEM Alert: {subject}"
    msg.set_content(str(log))
    
    await aiosmtplib.send(msg, hostname= "localhost", port = 1025)  # Dev Mail Server