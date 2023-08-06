from uuid import UUID

from fastapi import APIRouter, Depends

from cafe_api.services.menu_service import MenuService
from cafe_api.shemas import schemas

router = APIRouter()


@router.get('/menus', response_model=list[schemas.MenuOut], status_code=200)
def get_menus(menu_service: MenuService = Depends()):
    menus = menu_service.get_menus()
    return menus


@router.get('/menus/{target_menu_id}', response_model=schemas.MenuOut, status_code=200)
def get_menu(target_menu_id: UUID, menu_service: MenuService = Depends()):
    menu = menu_service.get_menu(menu_id=target_menu_id)
    if menu is None:
        return menu_service.menu_nf
    else:
        return menu


@router.post('/menus', response_model=schemas.MenuOut, status_code=201)
def create_menu(item_data: schemas.MenuIn, menu_service: MenuService = Depends()):
    return menu_service.create(item_data=item_data)


@router.patch('/menus/{target_menu_id}', response_model=schemas.MenuOut, status_code=200)
def update_menu(target_menu_id: UUID, item_data: schemas.MenuIn, menu_service: MenuService = Depends()):
    return menu_service.update(menu_id=target_menu_id, item_data=item_data)


@router.delete('/menus/{target_menu_id}', response_model=schemas.SomethingDelete)
def delete_menu(target_menu_id: UUID, menu_service: MenuService = Depends()):
    if menu_service.delete(menu_id=target_menu_id) is None:
        return {'status': True, 'detail': 'The menu has been deleted'}
    else:
        return {'status': False, 'detail': "The menu hasn't been deleted"}
