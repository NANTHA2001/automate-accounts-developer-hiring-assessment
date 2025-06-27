# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.endpoints import upload, validate, process, receipts
from app.db import models, session
from app.endpoints import dev_tools

# Create tables
models.Base.metadata.create_all(bind=session.engine)

app = FastAPI(title="Receipt Automation API")

# Allow CORS for frontend dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/upload")
app.include_router(validate.router, prefix="/validate")
app.include_router(process.router, prefix="/process")
app.include_router(receipts.router, prefix="/receipts")
app.include_router(dev_tools.router)
