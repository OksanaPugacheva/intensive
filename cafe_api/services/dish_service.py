from fastapi import Depends

from cafe_api.repository.dish_repository import DishRepository


class DishService:
    def __init__(self, db_repository: DishRepository = Depends()):
        self.db_repository = db_repository

    def create(self, submenu_id, item_data):
        item = self.db_repository.create(target_submenu_id=submenu_id, item_data=item_data)

        return item

    def update(self, dish_id, item_data):
        item = self.db_repository.update(target_dish_id=dish_id, item_data=item_data)

        return item

    def delete(self, dish_id):
        item = self.db_repository.delete(target_dish_id=dish_id)

        return item

    def get_dish(self, dish_id):
        item = self.db_repository.get_dish(target_dish_id=dish_id)

        return item

    def get_dishes(self, submenu_id):
        items = self.db_repository.get_dishes(target_submenu_id=submenu_id)

        return items
