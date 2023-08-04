from fastapi.responses import JSONResponse


def menu_answer(menu):
    return {'id': menu.id,
            'title': menu.title,
            'description': menu.description,
            'submenus_count': len(menu.submenus),
            'dishes_count': sum(len(oneSub.dishes) for oneSub in menu.submenus)}


def submenu_answer(submenu):
    return {'id': submenu.id,
            'title': submenu.title,
            'description': submenu.description,
            'dishes_count': len(submenu.dishes)}


def dish_answer(dish):
    return {'id': dish.id,
            'title': dish.title,
            'description': dish.description,
            'price': format(dish.price, '.2f')}


menu_nf = JSONResponse(status_code=404, content={'detail': 'menu not found'})
submenu_nf = JSONResponse(status_code=404, content={'detail': 'submenu not found'})
dish_nf = JSONResponse(status_code=404, content={'detail': 'dish not found'})
