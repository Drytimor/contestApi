from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(settings.POSTGRES_URL_ENGINE, echo=True)
sync_session_maker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = sync_session_maker()
    try:
        yield db
    finally:
        db.close()