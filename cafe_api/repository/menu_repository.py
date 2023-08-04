import uuid

from fastapi import Depends
from sqlalchemy.orm import Session

from cafe_api import schemas
from cafe_api.database import models
from cafe_api.database.db_connection import get_db


class MenuRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.model = models.Menu
        self.db = db

    def get_menus(self):
        menus = self.db.query(self.model)
        return menus.all()

    def get_menu(self, target_menu_id: uuid.UUID):
        menu = self.db.query(self.model).filter(self.model.id == target_menu_id).first()
        return menu

    def create_menu(self, item_data: schemas.MenuIn):
        db_menu = self.model(title=item_data.title, description=item_data.description)
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return db_menu

    def update_menu(self, target_menu_id: uuid.UUID, item_data: schemas.MenuIn):
        self.db.query(self.model).filter(self.model.id == target_menu_id).update(
            {'title': item_data.title, 'description': item_data.description})
        self.db.commit()
        return self.get_menu(target_menu_id=target_menu_id)

    def delete_menu(self, target_menu_id: uuid.UUID):
        menu = self.db.query(self.model).get(target_menu_id)
        if menu:
            self.db.delete(menu)
            self.db.commit()
        return self.get_menu(target_menu_id=target_menu_id)
