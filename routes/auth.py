from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from database import get_db
from models import APIKey
from schemas import APIKeyResponse
from utils.security import generate_api_key

router = APIRouter()


@router.post("/generate-key", response_model=APIKeyResponse)
def create_api_key(db: Session = Depends(get_db)):
    
    # Generate new API key
    new_key = generate_api_key()

    # Create DB object
    api_key_obj = APIKey(
        key=new_key,
        created_at=datetime.utcnow()
    )

    # Save to database
    db.add(api_key_obj)
    db.commit()
    db.refresh(api_key_obj)

    return api_key_obj