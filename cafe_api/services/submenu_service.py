import redis  # type: ignore
from fastapi import Depends
from fastapi.responses import JSONResponse

from cafe_api.repository.cache_repository import RedisCache, get_redis_client
from cafe_api.repository.submenu_repository import SubmenuRepository


class SubmenuService:
    def __init__(self, db_repository: SubmenuRepository = Depends(),
                 redis_client: redis.Redis = Depends(get_redis_client)):
        self.db_repository = db_repository
        self.cache_client = RedisCache(redis_client)
        self.submenu_nf = JSONResponse(status_code=404, content={'detail': 'submenu not found'})

    def create(self, menu_id, item_data):
        item = self.db_repository.create(target_menu_id=menu_id, item_data=item_data)
        self.cache_client.clear_after_change(menu_id)
        self.cache_client.set(f'{menu_id}:{item.id})', item)
        return item

    def update(self, menu_id, submenu_id, item_data):
        item = self.db_repository.update(target_submenu_id=submenu_id, item_data=item_data)
        self.cache_client.clear_after_change(menu_id)
        self.cache_client.set(f'{menu_id}:{submenu_id}', item)
        return item

    def delete(self, menu_id, submenu_id):
        item = self.db_repository.delete(target_submenu_id=submenu_id)
        self.cache_client.clear_after_change(menu_id)
        return item

    def get_submenu(self, menu_id, submenu_id):
        cached = self.cache_client.get(f'{menu_id}:{submenu_id}')
        if cached is not None:
            return cached
        else:
            item = self.db_repository.get_submenu(target_submenu_id=submenu_id)
            self.cache_client.set(f'{menu_id}:{submenu_id}', item)
            return item

    def get_submenus(self, menu_id):
        cached = self.cache_client.get(f'all:{menu_id}')
        if cached is not None:
            return cached
        else:
            items = self.db_repository.get_submenus(target_menu_id=menu_id)
            self.cache_client.set(f'all:{menu_id}', items)
            return items
