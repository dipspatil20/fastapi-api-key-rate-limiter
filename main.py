from fastapi import FastAPI
from database import engine, Base
import models

from routes import auth, protected

# Create tables
Base.metadata.create_all(bind=engine)

# ✅ FIRST create app
app = FastAPI()

# ✅ THEN include routers
app.include_router(auth.router)
app.include_router(protected.router)


@app.get("/")
def read_root():
    return {"message": "API is running"}