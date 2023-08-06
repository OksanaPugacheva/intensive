import redis  # type: ignore
from fastapi import Depends
from fastapi.responses import JSONResponse

from cafe_api.repository.cache_repository import RedisCache, get_redis_client
from cafe_api.repository.menu_repository import MenuRepository


class MenuService:
    def __init__(self, db_repository: MenuRepository = Depends(),
                 redis_client: redis.Redis = Depends(get_redis_client)):
        self.db_repository = db_repository
        self.cache_client = RedisCache(redis_client)
        self.menu_nf = JSONResponse(status_code=404, content={'detail': 'menu not found'})

    def create(self, item_data):
        item = self.db_repository.create_menu(item_data=item_data)
        self.cache_client.clear_after_change(item.id)
        self.cache_client.set(f'{item.id}', item)
        return item

    def update(self, menu_id, item_data):
        item = self.db_repository.update_menu(target_menu_id=menu_id, item_data=item_data)
        self.cache_client.clear_after_change(menu_id)
        self.cache_client.set(f'{item.id}', item)
        return item

    def delete(self, menu_id):
        item = self.db_repository.delete_menu(target_menu_id=menu_id)
        self.cache_client.clear_after_change(menu_id)
        return item

    def get_menu(self, menu_id):
        cached = self.cache_client.get(f'{menu_id}')
        if cached is not None:
            return cached
        else:
            item = self.db_repository.get_menu(target_menu_id=menu_id)
            self.cache_client.set(f'{menu_id}', item)
            return item

    def get_menus(self):
        cached = self.cache_client.get('all')
        if cached is not None:
            return cached
        else:
            items = self.db_repository.get_menus()
            self.cache_client.set('all', items)
            return items
