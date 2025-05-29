from pydantic import BaseModel, Field
from typing import Optional

class BaseLogModel(BaseModel):
    timestamp: str
    message: str
    source_ip: Optional[str]
    dest_ip: Optional[str]
    severity: Optional[str]