from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cafe_api.database import models

DATABASE_LOGIN = 'postgres'
DATABASE_PASSWORD = 'magic'
DATABASE_NAME = 'postgres'

engine = create_engine(f'postgresql://{DATABASE_LOGIN}:{DATABASE_PASSWORD}@localhost/{DATABASE_NAME}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
