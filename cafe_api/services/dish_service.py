import redis  # type: ignore
from fastapi import Depends
from fastapi.responses import JSONResponse

from cafe_api.repository.cache_repository import RedisCache, get_redis_client
from cafe_api.repository.dish_repository import DishRepository


class DishService:
    def __init__(self, db_repository: DishRepository = Depends(),
                 redis_client: redis.Redis = Depends(get_redis_client)):
        self.db_repository = db_repository
        self.cache_client = RedisCache(redis_client)
        self.dish_nf = JSONResponse(status_code=404, content={'detail': 'dish not found'})

    def create(self, menu_id, submenu_id, item_data):
        item = self.db_repository.create(target_submenu_id=submenu_id, item_data=item_data)
        self.cache_client.clear_after_change(menu_id)
        self.cache_client.set(f'{menu_id}:{submenu_id}:{item.id}', item)
        return item

    def update(self, menu_id, submenu_id, dish_id, item_data):
        item = self.db_repository.update(target_dish_id=dish_id, item_data=item_data)
        self.cache_client.clear_after_change(menu_id)
        self.cache_client.set(f'{menu_id}:{submenu_id}:{dish_id}', item)
        return item

    def delete(self, menu_id, dish_id):
        item = self.db_repository.delete(target_dish_id=dish_id)
        self.cache_client.clear_after_change(menu_id)
        return item

    def get_dish(self, menu_id, submenu_id, dish_id):
        cached = self.cache_client.get(f'{menu_id}:{submenu_id}:{dish_id}')
        if cached is not None:
            return cached
        else:
            item = self.db_repository.get_dish(target_dish_id=dish_id)
            self.cache_client.set(f'{menu_id}:{submenu_id}:{dish_id}', item)
            return item

    def get_dishes(self, menu_id, submenu_id):
        cached = self.cache_client.get(f'all:{menu_id}:{submenu_id}')
        if cached is not None:
            return cached
        else:
            items = self.db_repository.get_dishes(target_submenu_id=submenu_id)
            self.cache_client.set(f'all:{menu_id}:{submenu_id}', items)
            return items
