import uuid

from fastapi import Depends
from sqlalchemy import distinct, func, select
from sqlalchemy.orm import Session

from cafe_api.database.db_connection import get_db
from cafe_api.database.models import Dish, Menu, Submenu
from cafe_api.shemas import schemas


class MenuRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.model = Menu
        self.db = db

    def get_menus(self):
        q = self.db.execute(
            select(
                Menu.id,
                Menu.title,
                Menu.description,
                func.count(distinct(Submenu.id)).label('submenus_count'),
                func.count(distinct(Dish.id)).label('dishes_count'),
            )
            .outerjoin(Submenu, Menu.id == Submenu.menu_id)
            .outerjoin(Dish, Submenu.id == Dish.submenu_id)
            .group_by(Menu.id)
        )
        return q.all()

    def get_menu(self, target_menu_id: uuid.UUID):
        menu = self.db.execute(
            select(
                Menu.id,
                Menu.title,
                Menu.description,
                func.count(distinct(Submenu.id)).label('submenus_count'),
                func.count(distinct(Dish.id)).label('dishes_count'),
            )
            .outerjoin(Submenu, Menu.id == Submenu.menu_id)
            .outerjoin(Dish, Submenu.id == Dish.submenu_id)
            .group_by(Menu.id)
            .filter(Menu.id == target_menu_id)
        )
        return menu.first()

    def create_menu(self, item_data: schemas.MenuIn):
        db_menu = self.model(title=item_data.title, description=item_data.description)
        self.db.add(db_menu)
        self.db.commit()
        self.db.refresh(db_menu)
        return self.get_menu(db_menu.id)

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
