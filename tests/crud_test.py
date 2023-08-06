from api import CRUD

MENU_ID = None
MENU_TITLE = None
MENU_DESCRIPTION = None
SUBMENU_ID = None
SUBMENU_TITLE = None
SUBMENU_DESCRIPTION = None
DISH_ID = None
DISH_TITLE = None
DISH_DESCRIPTION = None
DISH_PRICE = None


class TestCRUDmenu:
    def test_get_menus(self):
        response = CRUD().get_menus()
        assert response.status_code == 200
        assert response.json() == []

    def test_post_menu(self):
        body = {'title': 'My menu 1', 'description': 'My menu description 1'}
        response = CRUD().post_menu(body=body)
        assert response.status_code == 201
        global MENU_ID, MENU_TITLE, MENU_DESCRIPTION
        MENU_ID = response.json()['id']
        MENU_TITLE = response.json()['title']
        MENU_DESCRIPTION = response.json()['description']

    def test_get_menus_after_create(self):
        response = CRUD().get_menus()
        assert response.status_code == 200
        assert response.json() != []

    def test_get_menu(self):
        response = CRUD().get_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == MENU_ID
        assert response.json()['title'] == MENU_TITLE
        assert response.json()['description'] == MENU_DESCRIPTION

    def test_patch_menu(self):
        menu_title_update = 'My menu update 1'
        menu_description_update = 'My menu update description 1'
        body = {'title': f'{menu_title_update}',
                'description': f'{menu_description_update}'}
        response = CRUD().patch_menu(MENU_ID, body=body)
        assert response.status_code == 200
        assert response.json()['id'] == MENU_ID
        assert response.json()['title'] == menu_title_update
        assert response.json()['description'] == menu_description_update
        global MENU_TITLE, MENU_DESCRIPTION
        MENU_TITLE = menu_title_update
        MENU_DESCRIPTION = menu_description_update

    def test_get_menu_after_update(self):
        response = CRUD().get_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == MENU_ID
        assert response.json()['title'] == MENU_TITLE
        assert response.json()['description'] == MENU_DESCRIPTION

    def test_delete_menu(self):
        response = CRUD().delete_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The menu has been deleted'

    def test_get_menus_after_delete(self):
        response = CRUD().get_menus()
        assert response.status_code == 200
        assert response.json() == []

    def test_get_menu_after_delete(self):
        response = CRUD().get_menu(MENU_ID)
        assert response.status_code == 404
        assert response.json()['detail'] == 'menu not found'


class TestCRUDSubmenu:
    def test_post_menu(self):
        body = {'title': 'My menu 1', 'description': 'My menu description 1'}
        response = CRUD().post_menu(body=body)
        assert response.status_code == 201
        global MENU_ID
        MENU_ID = response.json()['id']

    def test_get_submenus(self):
        response = CRUD().get_submenus(MENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_post_submenus(self):
        body = {'title': 'My submenu 1', 'description': 'My submenu description 1'}
        response = CRUD().post_submenu(MENU_ID, body=body)
        assert response.status_code == 201
        global SUBMENU_ID, SUBMENU_DESCRIPTION, SUBMENU_TITLE
        SUBMENU_ID = response.json()['id']
        SUBMENU_TITLE = response.json()['title']
        SUBMENU_DESCRIPTION = response.json()['description']

    def test_get_submenus_after_create(self):
        response = CRUD().get_submenus(MENU_ID)
        assert response.status_code == 200
        assert response.json() != []

    def test_get_submenu(self):
        response = CRUD().get_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == SUBMENU_ID
        assert response.json()['title'] == SUBMENU_TITLE
        assert response.json()['description'] == SUBMENU_DESCRIPTION

    def test_patch_submenu(self):
        submenu_title_update = 'My submenu update 1'
        submenu_description_update = 'My submenu update description 1'
        body = {'title': f'{submenu_title_update}',
                'description': f'{submenu_description_update}'}
        response = CRUD().patch_submenu(MENU_ID, SUBMENU_ID, body=body)
        assert response.status_code == 200
        assert response.json()['id'] == SUBMENU_ID
        assert response.json()['title'] == submenu_title_update
        assert response.json()['description'] == submenu_description_update
        global SUBMENU_TITLE, SUBMENU_DESCRIPTION
        SUBMENU_TITLE = submenu_title_update
        SUBMENU_DESCRIPTION = submenu_description_update

    def test_get_submenu_after_update(self):
        response = CRUD().get_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == SUBMENU_ID
        assert response.json()['title'] == SUBMENU_TITLE
        assert response.json()['description'] == SUBMENU_DESCRIPTION

    def test_delete_submenu(self):
        response = CRUD().delete_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The submenu has been deleted'

    def test_get_submenus_after_delete(self):
        response = CRUD().get_submenus(MENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_submenu_after_delete(self):
        response = CRUD().get_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 404
        assert response.json()['detail'] == 'submenu not found'

    def test_delete_menu(self):
        response = CRUD().delete_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The menu has been deleted'


class TestCRUDDish:
    def test_post_menu(self):
        body = {'title': 'My menu 1', 'description': 'My menu description 1'}
        response = CRUD().post_menu(body=body)
        assert response.status_code == 201
        global MENU_ID
        MENU_ID = response.json()['id']

    def test_post_submenus(self):
        body = {'title': 'My submenu 1', 'description': 'My submenu description 1'}
        response = CRUD().post_submenu(MENU_ID, body=body)
        assert response.status_code == 201
        global SUBMENU_ID
        SUBMENU_ID = response.json()['id']

    def test_get_dishes(self):
        response = CRUD().get_dishes(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_post_dish(self):
        body = {'title': 'My dish 1', 'description': 'My dish description', 'price': '2.22'}
        response = CRUD().post_dish(MENU_ID, SUBMENU_ID, body=body)
        assert response.status_code == 201
        global DISH_ID, DISH_TITLE, DISH_DESCRIPTION, DISH_PRICE
        DISH_ID = response.json()['id']
        DISH_TITLE = response.json()['title']
        DISH_DESCRIPTION = response.json()['description']
        DISH_PRICE = response.json()['price']

    def test_get_dishes_after_create(self):
        response = CRUD().get_dishes(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json() != []

    def test_get_dish(self):
        response = CRUD().get_dish(MENU_ID, SUBMENU_ID, DISH_ID)
        assert response.status_code == 200
        assert response.json()['id'] == DISH_ID
        assert response.json()['title'] == DISH_TITLE
        assert response.json()['description'] == DISH_DESCRIPTION
        assert response.json()['price'] == DISH_PRICE

    def test_patch_dish(self):
        dish_title_update = 'My update dish 1'
        dish_description_update = 'My submenu update description 1'
        dish_price_update = '3.33'
        body = {'title': f'{dish_title_update}', 'description': f'{dish_description_update}',
                'price': f'{dish_price_update}'}
        response = CRUD().patch_dish(MENU_ID, SUBMENU_ID, DISH_ID, body)
        assert response.status_code == 200
        assert response.json()['id'] == DISH_ID
        assert response.json()['title'] == dish_title_update
        assert response.json()['description'] == dish_description_update
        assert response.json()['price'] == dish_price_update
        global DISH_TITLE, DISH_DESCRIPTION, DISH_PRICE
        DISH_TITLE = dish_title_update
        DISH_DESCRIPTION = dish_description_update
        DISH_PRICE = dish_price_update

    def test_get_dish_after_update(self):
        response = CRUD().get_dish(MENU_ID, SUBMENU_ID, DISH_ID)
        assert response.status_code == 200
        assert response.json()['id'] == DISH_ID
        assert response.json()['title'] == DISH_TITLE
        assert response.json()['description'] == DISH_DESCRIPTION
        assert response.json()['price'] == DISH_PRICE

    def test_delete_dish(self):
        response = CRUD().delete_dish(MENU_ID, SUBMENU_ID, DISH_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The dish has been deleted'

    def test_get_dishes_after_delete(self):
        response = CRUD().get_dishes(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_dish_after_delete(self):
        response = CRUD().get_dish(MENU_ID, SUBMENU_ID, DISH_ID)
        assert response.status_code == 404
        assert response.json()['detail'] == 'dish not found'

    def test_delete_submenu(self):
        response = CRUD().delete_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The submenu has been deleted'

    def test_delete_menu(self):
        response = CRUD().delete_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The menu has been deleted'


class TestCountSubmenusAndDishes:
    def test_post_menu(self):
        body = {'title': 'My menu 1', 'description': 'My menu description 1'}
        response = CRUD().post_menu(body=body)
        assert response.status_code == 201
        global MENU_ID
        MENU_ID = response.json()['id']

    def test_post_submenus(self):
        body = {'title': 'My submenu 1', 'description': 'My submenu description 1'}
        response = CRUD().post_submenu(MENU_ID, body=body)
        assert response.status_code == 201
        global SUBMENU_ID
        SUBMENU_ID = response.json()['id']

    def test_post_dish_one(self):
        body = {'title': 'My dish 1', 'description': 'My dish 1 description', 'price': '2.22'}
        response = CRUD().post_dish(MENU_ID, SUBMENU_ID, body=body)
        assert response.status_code == 201

    def test_post_dish_two(self):
        body = {'title': 'My dish 2', 'description': 'My dish 2 description', 'price': '4.44'}
        response = CRUD().post_dish(MENU_ID, SUBMENU_ID, body=body)
        assert response.status_code == 201

    def test_get_menu(self):
        response = CRUD().get_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == MENU_ID
        assert response.json()['submenus_count'] == 1
        assert response.json()['dishes_count'] == 2

    def test_get_submenu(self):
        response = CRUD().get_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == SUBMENU_ID
        assert response.json()['dishes_count'] == 2

    def test_delete_submenu(self):
        response = CRUD().delete_submenu(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The submenu has been deleted'

    def test_get_submenus_after_delete(self):
        response = CRUD().get_submenus(MENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_dishes_after_delete_submenu(self):
        response = CRUD().get_dishes(MENU_ID, SUBMENU_ID)
        assert response.status_code == 200
        assert response.json() == []

    def test_get_menu_after_delete_submenu(self):
        response = CRUD().get_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['id'] == MENU_ID
        assert response.json()['submenus_count'] == 0
        assert response.json()['dishes_count'] == 0

    def test_delete_menu(self):
        response = CRUD().delete_menu(MENU_ID)
        assert response.status_code == 200
        assert response.json()['status'] is True
        assert response.json()['detail'] == 'The menu has been deleted'

    def test_get_menus(self):
        response = CRUD().get_menus()
        assert response.status_code == 200
        assert response.json() == []
