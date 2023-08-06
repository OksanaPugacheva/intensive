from uuid import UUID

from fastapi import APIRouter, Depends

from cafe_api.services.submenu_service import SubmenuService
from cafe_api.shemas import schemas

router = APIRouter()


@router.post('/submenus', response_model=schemas.SubmenuOut, status_code=201)
def create_submenu(target_menu_id: UUID, item_data: schemas.SubmenuIn, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.create(menu_id=target_menu_id, item_data=item_data)
    return submenu


@router.get('/submenus/{target_submenu_id}', response_model=schemas.SubmenuOut)
def get_submenu(target_menu_id: UUID, target_submenu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.get_submenu(menu_id=target_menu_id, submenu_id=target_submenu_id)
    if submenu is None:
        return submenu_service.submenu_nf
    return submenu


@router.get('/submenus', response_model=list[schemas.SubmenuOut])
def get_submenus(target_menu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenus = submenu_service.get_submenus(menu_id=target_menu_id)
    return submenus


@router.patch('/submenus/{target_submenu_id}', response_model=schemas.SubmenuOut)
def update_submenu(target_menu_id: UUID, target_submenu_id: UUID, item_data: schemas.SubmenuIn,
                   submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.update(menu_id=target_menu_id, submenu_id=target_submenu_id, item_data=item_data)
    if submenu is None:
        return submenu_service.submenu_nf
    return submenu


@router.delete('/submenus/{target_submenu_id}', response_model=schemas.SomethingDelete)
def delete_submenu(target_menu_id: UUID, target_submenu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.delete(menu_id=target_menu_id, submenu_id=target_submenu_id)
    if submenu is None:
        return {'status': True, 'detail': 'The submenu has been deleted'}
    else:
        return {'status': False, 'detail': "The submenu hasn't been deleted"}
