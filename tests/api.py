import requests


class CRUD:
    LOCAL_URL = "http://127.0.0.1:8000"
    MENUS_URL = "/api/v1/menus"
    SUBMENUS_URL = "/submenus"
    DISHES_URL = "/dishes"

    def get_menus(self):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}")
        return response

    def get_menu(self, menu_id):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}")
        return response

    def post_menu(self, body):
        response = requests.post(f"{self.LOCAL_URL}{self.MENUS_URL}", json=body)
        return response

    def patch_menu(self, menu_id, body):
        response = requests.patch(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}", json=body)
        return response

    def delete_menu(self, menu_id):
        response = requests.delete(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}")
        return response

    def get_submenus(self, menu_id):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}")
        return response

    def get_submenu(self, menu_id, submenu_id):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}")
        return response

    def post_submenu(self, menu_id, body):
        response = requests.post(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}", json=body)
        return response

    def patch_submenu(self, menu_id, submenu_id, body):
        response = requests.patch(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}", json=body)
        return response

    def delete_submenu(self, menu_id, submenu_id):
        response = requests.delete(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}")
        return response

    def get_dishes(self, menu_id, submenu_id):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}{self.DISHES_URL}")
        return response

    def get_dish(self, menu_id, submenu_id, dish_id):
        response = requests.get(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}"
                                f"{self.DISHES_URL}/{dish_id}")
        return response

    def post_dish(self, menu_id, submenu_id, body):
        response = requests.post(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}"
                                 f"{self.DISHES_URL}", json=body)
        return response

    def patch_dish(self, menu_id, submenu_id, dish_id, body):
        response = requests.patch(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}"
                                  f"{self.DISHES_URL}/{dish_id}", json=body)
        return response

    def delete_dish(self, menu_id, submenu_id, dish_id):
        response = requests.delete(f"{self.LOCAL_URL}{self.MENUS_URL}/{menu_id}{self.SUBMENUS_URL}/{submenu_id}"
                                   f"{self.DISHES_URL}/{dish_id}")
        return response
