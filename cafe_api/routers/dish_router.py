from uuid import UUID

from fastapi import APIRouter, Depends

from cafe_api import answer, schemas
from cafe_api.services.dish_service import DishService

router = APIRouter()


@router.get('/dishes/{target_dish_id}', response_model=schemas.DishOut)
def get_dish(target_dish_id: UUID, dish_service: DishService = Depends()):
    dish = dish_service.get_dish(dish_id=target_dish_id)
    if dish is None:
        return answer.dish_nf
    return answer.dish_answer(dish)


@router.get('/dishes', response_model=list[schemas.DishOut])
def get_dishes(target_submenu_id: UUID, dish_service: DishService = Depends()):
    dishes = dish_service.get_dishes(submenu_id=target_submenu_id)
    dishes_list = list()
    for dish in dishes:
        dishes_list.append(answer.dish_answer(dish))
    return dishes_list


@router.post('/dishes', response_model=schemas.DishOut, status_code=201)
def create_dish(target_submenu_id: UUID, item_data: schemas.DishIn, dish_service: DishService = Depends()):
    dish = dish_service.create(submenu_id=target_submenu_id, item_data=item_data)
    if dish is None:
        return answer.dish_nf
    return answer.dish_answer(dish)


@router.patch('/dishes/{target_dish_id}', response_model=schemas.DishOut,)
def update_dish(target_dish_id: UUID, item_data: schemas.DishIn, dish_service: DishService = Depends()):
    dish = dish_service.update(dish_id=target_dish_id, item_data=item_data)
    if dish is None:
        return answer.dish_nf
    return answer.dish_answer(dish)


@router.delete('/dishes/{target_dish_id}', response_model=schemas.SomethingDelete)
def delete_submenu(target_dish_id: UUID, dish_service: DishService = Depends()):
    dish = dish_service.delete(dish_id=target_dish_id)
    if dish is None:
        return {'status': True, 'detail': 'The dish has been deleted'}
    else:
        return {'status': False, 'detail': "The dish hasn't been deleted"}
