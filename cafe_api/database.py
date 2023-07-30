from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


DATABASE_LOGIN = "postgres"
DATABASE_PASSWORD = "magic"
DATABASE_NAME = "postgres"

engine = create_engine(f"postgresql://{DATABASE_LOGIN}:{DATABASE_PASSWORD}@db/{DATABASE_NAME}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
