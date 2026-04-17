from fastapi import APIRouter, Depends, Header
from sqlalchemy.orm import Session

from database import get_db
from utils.rate_limiter import check_rate_limit

# ✅ THIS IS REQUIRED
router = APIRouter()


@router.get("/data")
def get_protected_data(
    x_api_key: str = Header(...),
    db: Session = Depends(get_db)
):
    check_rate_limit(x_api_key, db)

    return {
        "message": "Access granted",
        "data": "This is protected data"
    }