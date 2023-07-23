from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


DATABASE_LOGIN = "ChangeMe"
DATABASE_PASSWORD = "ChangeMe"
DATABASE_NAME = "ChangeMe"

engine = create_engine(f"postgresql://{DATABASE_LOGIN}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass
