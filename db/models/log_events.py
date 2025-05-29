from sqlalchemy import Column, String, DateTime, Integer
from db.db import Base
from datetime import datetime


class LogEvent(Base):
    __tablename__ = "log_events"
    
    id = Column(Integer, default = datetime.timezone.utc)
    timestamp = Column(DateTime, default= datetime.timezone.utc)
    message = Column(String)
    source = Column(String)
    source_ip = Column(String, nullable = True)
    dest_ip = Column(String, nullable = True)
    severity = Column(String, nullable = True)
    
