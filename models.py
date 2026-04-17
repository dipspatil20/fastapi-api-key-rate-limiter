from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, index=True)

    # Unique API key
    key = Column(String, unique=True, index=True, nullable=False)

    # When key was created
    created_at = Column(DateTime, default=datetime.utcnow)

    # Number of requests made
    request_count = Column(Integer, default=0)

    # Last request timestamp
    last_request_time = Column(DateTime, nullable=True)