from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL =os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/face_recognition")  # "postgresql://user:password@db_host/db_name"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class FaceDetectionResult(Base):
    __tablename__ = "face_detection"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    result = Column(JSON, nullable=True)  # 這裡設置為可為空

def save_to_db(filename, analysis):
    db = SessionLocal()
    db_result = FaceDetectionResult(filename=filename, result=analysis)
    db.add(db_result)
    db.commit()
    db.close()