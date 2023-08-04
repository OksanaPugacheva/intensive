import uuid

from fastapi import Depends
from sqlalchemy.orm import Session

from cafe_api import schemas
from cafe_api.db import models
from cafe_api.db.database import get_db


class DishRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.model = models.Dish
        self.db = db

    def get_dishes(self, target_submenu_id: uuid.UUID) -> list[type[models.Dish]]:
        submenu = self.db.query(models.Submenu).filter(models.Submenu.id == target_submenu_id).first()
        if submenu is None:
            return []
        return submenu.dishes

    def get_dish(self, target_dish_id: uuid.UUID) -> models.Dish:
        dish = self.db.query(self.model).filter(self.model.id == target_dish_id).first()
        return dish

    def create(self, target_submenu_id: uuid.UUID, item_data: schemas.DishIn) -> models.Dish:
        db_dish = models.Dish(title=item_data.title,
                              description=item_data.description,
                              price=item_data.price,
                              submenu_id=target_submenu_id)
        self.db.add(db_dish)
        self.db.commit()
        self.db.refresh(db_dish)
        return self.get_dish(target_dish_id=db_dish.id)

    def update(self, target_dish_id: uuid.UUID, item_data: schemas.SubmenuIn) \
            -> models.Dish:
        self.db.query(self.model).filter(self.model.id == target_dish_id).update(
            {'title': item_data.title, 'description': item_data.description, 'price': item_data.price})
        self.db.commit()
        return self.get_dish(target_dish_id=target_dish_id)

    def delete(self, target_dish_id: uuid.UUID) -> models.Dish:
        dish = self.db.query(self.model).get(target_dish_id)
        if dish:
            self.db.delete(dish)
            self.db.commit()
        return self.get_dish(target_dish_id=target_dish_id)
