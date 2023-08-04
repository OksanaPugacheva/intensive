from fastapi import Depends

from cafe_api.repository.menu_repository import MenuRepository


class MenuService:
    def __init__(self, db_repository: MenuRepository = Depends()):
        self.db_repository = db_repository

    def create(self, item_data):
        item = self.db_repository.create_menu(item_data=item_data)

        return item

    def update(self, menu_id, item_data):
        item = self.db_repository.update_menu(target_menu_id=menu_id, item_data=item_data)

        return item

    def delete(self, menu_id):
        item = self.db_repository.delete_menu(target_menu_id=menu_id)

        return item

    def get_menu(self, menu_id):
        item = self.db_repository.get_menu(target_menu_id=menu_id)

        return item

    def get_menus(self):
        items = self.db_repository.get_menus()

        return items
