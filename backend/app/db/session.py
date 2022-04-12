from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.core.settings import SQLALCHEMY_DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
