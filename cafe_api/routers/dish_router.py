from uuid import UUID

from fastapi import APIRouter, Depends

from cafe_api.services.dish_service import DishService
from cafe_api.shemas import schemas

router = APIRouter()


@router.get('/dishes/{target_dish_id}', response_model=schemas.DishOut)
def get_dish(target_menu_id: UUID, target_submenu_id: UUID, target_dish_id: UUID,
             dish_service: DishService = Depends()):
    dish = dish_service.get_dish(menu_id=target_menu_id, submenu_id=target_submenu_id, dish_id=target_dish_id)
    if dish is None:
        return dish_service.dish_nf
    return dish


@router.get('/dishes', response_model=list[schemas.DishOut])
def get_dishes(target_menu_id: UUID, target_submenu_id: UUID, dish_service: DishService = Depends()):
    dishes = dish_service.get_dishes(menu_id=target_menu_id, submenu_id=target_submenu_id)
    return dishes


@router.post('/dishes', response_model=schemas.DishOut, status_code=201)
def create_dish(target_menu_id: UUID, target_submenu_id: UUID, item_data: schemas.DishIn,
                dish_service: DishService = Depends()):
    dish = dish_service.create(menu_id=target_menu_id, submenu_id=target_submenu_id, item_data=item_data)
    if dish is None:
        return dish_service.dish_nf
    return dish


@router.patch('/dishes/{target_dish_id}', response_model=schemas.DishOut, )
def update_dish(target_menu_id: UUID, target_submenu_id: UUID, target_dish_id: UUID, item_data: schemas.DishIn,
                dish_service: DishService = Depends()):
    dish = dish_service.update(menu_id=target_menu_id, submenu_id=target_submenu_id, dish_id=target_dish_id,
                               item_data=item_data)
    if dish is None:
        return dish_service.dish_nf
    return dish


@router.delete('/dishes/{target_dish_id}', response_model=schemas.SomethingDelete)
def delete_submenu(target_menu_id: UUID, target_dish_id: UUID, dish_service: DishService = Depends()):
    dish = dish_service.delete(menu_id=target_menu_id, dish_id=target_dish_id)
    if dish is None:
        return {'status': True, 'detail': 'The dish has been deleted'}
    else:
        return {'status': False, 'detail': "The dish hasn't been deleted"}
