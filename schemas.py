from pydantic import BaseModel
from datetime import datetime


# Response when API key is generated
class APIKeyResponse(BaseModel):
    key: str
    created_at: datetime


# Optional: For showing usage info
class APIKeyUsage(BaseModel):
    key: str
    request_count: int
    last_request_time: datetime | None