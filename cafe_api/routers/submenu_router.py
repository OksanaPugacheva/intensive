from uuid import UUID

from fastapi import APIRouter, Depends

from cafe_api import answer, schemas
from cafe_api.services.submenu_service import SubmenuService

router = APIRouter()


@router.post('/submenus', status_code=201)
def create_submenu(target_menu_id: UUID, item_data: schemas.SubmenuIn, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.create(menu_id=target_menu_id, item_data=item_data)
    if submenu is None:
        return answer.submenu_nf
    return answer.submenu_answer(submenu)


@router.get('/submenus/{target_submenu_id}', response_model=schemas.SubmenuOut)
def get_submenu(target_submenu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.get_submenu(submenu_id=target_submenu_id)
    if submenu is None:
        return answer.submenu_nf
    return answer.submenu_answer(submenu)


@router.get('/submenus', response_model=list[schemas.SubmenuOut])
def get_submenus(target_menu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenus = submenu_service.get_submenus(menu_id=target_menu_id)
    submenus_list = list()
    for submenu in submenus:
        submenus_list.append(answer.submenu_answer(submenu))
    return submenus_list


@router.patch('/submenus/{target_submenu_id}')
def update_submenu(target_menu_id: UUID, target_submenu_id: UUID, item_data: schemas.SubmenuIn,
                   submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.update(submenu_id=target_submenu_id, item_data=item_data)
    if submenu is None:
        return answer.menu_nf
    return answer.submenu_answer(submenu)


@router.delete('/submenus/{target_submenu_id}', response_model=schemas.SomethingDelete)
def delete_submenu(target_menu_id: UUID, target_submenu_id: UUID, submenu_service: SubmenuService = Depends()):
    submenu = submenu_service.delete(submenu_id=target_submenu_id)
    if target_menu_id:
        if submenu is None:
            return {'status': True, 'detail': 'The submenu has been deleted'}
        else:
            return {'status': False, 'detail': "The submenu hasn't been deleted"}
