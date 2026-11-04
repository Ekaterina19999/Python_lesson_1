from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# ⚠️ Убедись, что тут указан твой правильный пароль и база QA
DATABASE_URL = "postgresql://postgres:sS124@localhost:5432/QA"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_title = Column(String, nullable=False)
