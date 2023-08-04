from fastapi import Depends

from cafe_api.repository.submenu_repository import SubmenuRepository


class SubmenuService:
    def __init__(self, db_repository: SubmenuRepository = Depends()):
        self.db_repository = db_repository

    def create(self, menu_id, item_data):
        item = self.db_repository.create(target_menu_id=menu_id, item_data=item_data)

        return item

    def update(self, submenu_id, item_data):
        item = self.db_repository.update(target_submenu_id=submenu_id, item_data=item_data)

        return item

    def delete(self, submenu_id):
        item = self.db_repository.delete(target_submenu_id=submenu_id)

        return item

    def get_submenu(self, submenu_id):
        item = self.db_repository.get_submenu(target_submenu_id=submenu_id)

        return item

    def get_submenus(self, menu_id):
        items = self.db_repository.get_submenus(target_menu_id=menu_id)

        return items
