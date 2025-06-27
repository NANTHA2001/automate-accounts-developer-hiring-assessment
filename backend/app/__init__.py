# backend/app/db/init_db.py

from app.db.models import Base
from app.db.session import engine

def init():
    Base.metadata.create_all(bind=engine)
