import uuid

from fastapi import Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from cafe_api.database.db_connection import get_db
from cafe_api.database.models import Dish, Submenu
from cafe_api.shemas import schemas


class SubmenuRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.model = Submenu
        self.db = db

    def get_submenus(self, target_menu_id: uuid.UUID):
        submenu = self.db.execute(
            select(
                Submenu.id,
                Submenu.title,
                Submenu.description,
                func.count(Dish.id).label('dishes_count'),
            )
            .outerjoin(Dish)
            .group_by(Submenu.id)
            .filter(Submenu.menu_id == target_menu_id)
        )
        return submenu.all()

    def get_submenu(self, target_submenu_id: uuid.UUID):
        submenu = self.db.execute(
            select(
                Submenu.id,
                Submenu.title,
                Submenu.description,
                func.count(Dish.id).label('dishes_count'),
            )
            .outerjoin(Dish)
            .group_by(Submenu.id)
            .filter(Submenu.id == target_submenu_id)
        )
        return submenu.first()

    def create(self, target_menu_id: uuid.UUID, item_data: schemas.SubmenuIn):
        db_submenu = self.model(title=item_data.title,
                                description=item_data.description,
                                menu_id=target_menu_id)
        self.db.add(db_submenu)
        self.db.commit()
        self.db.refresh(db_submenu)
        return self.get_submenu(db_submenu.id)

    def update(self, target_submenu_id: uuid.UUID, item_data: schemas.SubmenuIn):
        self.db.query(self.model).filter(self.model.id == target_submenu_id).update(
            {'title': item_data.title, 'description': item_data.description})
        self.db.commit()
        return self.get_submenu(target_submenu_id=target_submenu_id)

    def delete(self, target_submenu_id: uuid.UUID):
        submenu = self.db.query(self.model).get(target_submenu_id)
        if submenu:
            self.db.delete(submenu)
            self.db.commit()
        return self.get_submenu(target_submenu_id=target_submenu_id)
