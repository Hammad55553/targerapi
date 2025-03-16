from sqlalchemy import create_engine, Column, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid
from datetime import datetime

# PostgreSQL Connection URL (Neon.tech ya apna local database use karein)
DATABASE_URL = "postgresql://neondb_owner:CeDyTMfmad79@ep-sparkling-bar-a5daghxj-pooler.us-east-2.aws.neon.tech/signup?sslmode=require"

# SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# SessionLocal Define Karna
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class UserData(Base):
    __tablename__ = "user_data"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    ip_address = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    user_agent = Column(String)
    referrer = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    education = Column(String)
    university = Column(String)
    country = Column(String)
    province = Column(String)
    city = Column(String)
    phone_number = Column(String)
    email = Column(String)
    timestamp = Column(DateTime, default=datetime.now)

# Database Tables Create Karna
Base.metadata.create_all(bind=engine)
