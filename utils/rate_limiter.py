from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from models import APIKey


# Rate limit config
REQUEST_LIMIT = 5
TIME_WINDOW = 60  # seconds


def check_rate_limit(api_key: str, db: Session):
    
    # 1. Check API key exists
    key_obj = db.query(APIKey).filter(APIKey.key == api_key).first()

    if not key_obj:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    current_time = datetime.utcnow()

    # 2. First request case
    if not key_obj.last_request_time:
        key_obj.last_request_time = current_time
        key_obj.request_count = 1
        db.commit()
        return key_obj

    # 3. Check time difference
    time_diff = (current_time - key_obj.last_request_time).total_seconds()

    if time_diff < TIME_WINDOW:
        # Same window
        if key_obj.request_count >= REQUEST_LIMIT:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later."
            )
        else:
            key_obj.request_count += 1
    else:
        # New time window → reset count
        key_obj.request_count = 1
        key_obj.last_request_time = current_time

    # 4. Save updates
    key_obj.last_request_time = current_time
    db.commit()

    return key_obj