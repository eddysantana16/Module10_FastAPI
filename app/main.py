from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users

app = FastAPI()

# Create DB tables
Base.metadata.create_all(bind=engine)

# Register the user router
app.include_router(users.router, prefix="/api", tags=["Users"])
