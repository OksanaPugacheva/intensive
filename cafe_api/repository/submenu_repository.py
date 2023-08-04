import uuid

from fastapi import Depends
from sqlalchemy.orm import Session

from cafe_api import schemas
from cafe_api.database import models
from cafe_api.database.db_connection import get_db


class SubmenuRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.model = models.Submenu
        self.db = db

    def get_submenus(self, target_menu_id: uuid.UUID) -> list[type[models.Submenu]]:
        menu = self.db.query(models.Menu).filter(models.Menu.id == target_menu_id).first()
        if menu is None:
            return []
        return menu.submenus

    def get_submenu(self, target_submenu_id: uuid.UUID) -> models.Submenu:
        submenu = self.db.query(self.model).filter(self.model.id == target_submenu_id).first()
        return submenu

    def create(self, target_menu_id: uuid.UUID, item_data: schemas.SubmenuIn) -> models.Submenu:
        db_submenu = self.model(title=item_data.title,
                                description=item_data.description,
                                menu_id=target_menu_id)
        self.db.add(db_submenu)
        self.db.commit()
        self.db.refresh(db_submenu)
        return self.get_submenu(target_submenu_id=db_submenu.id)

    def update(self, target_submenu_id: uuid.UUID, item_data: schemas.SubmenuIn) \
            -> models.Submenu:
        self.db.query(self.model).filter(self.model.id == target_submenu_id).update(
            {'title': item_data.title, 'description': item_data.description})
        self.db.commit()
        return self.get_submenu(target_submenu_id=target_submenu_id)

    def delete(self, target_submenu_id: uuid.UUID) -> models.Submenu:
        submenu = self.db.query(self.model).get(target_submenu_id)
        if submenu:
            self.db.delete(submenu)
            self.db.commit()
        return self.get_submenu(target_submenu_id=target_submenu_id)
