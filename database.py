from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

DATABASE_URL = "mysql+pymysql://root:36%40ASAD@localhost:3306/db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# This is the missing function
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
