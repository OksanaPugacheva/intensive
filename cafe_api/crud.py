from sqlalchemy.orm import Session
import uuid

import cafe_api.models as models
import cafe_api.schemas as schemas


def get_menu(target_menu_id: uuid.UUID, db: Session):
    menu = db.query(models.Menu).filter(models.Menu.id == target_menu_id).first()
    return menu


def get_menus(db: Session):
    menus = db.query(models.Menu).all()
    return menus


def create_menu(db: Session, menu: schemas.MenuIn):
    db_menu = models.Menu(title=menu.title, description=menu.description)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return get_menu(target_menu_id=db_menu.id, db=db)


def update_menu(target_menu_id: uuid.UUID, menu: schemas.MenuIn, db: Session):
    db.query(models.Menu).filter(models.Menu.id == target_menu_id).update(
        {'title': menu.title, 'description': menu.description})
    db.commit()
    return get_menu(target_menu_id=target_menu_id, db=db)


def delete_menu(target_menu_id: uuid.UUID, db: Session):
    menu = db.query(models.Menu).get(target_menu_id)
    if menu:
        db.delete(menu)
        db.commit()
    return get_menu(target_menu_id=target_menu_id, db=db)


def get_submenu(target_menu_id: uuid.UUID, target_submenu_id: uuid.UUID, db: Session):
    menu = db.query(models.Submenu).filter(models.Menu.id == target_menu_id).first()
    if menu is None:
        return None
    submenu = db.query(models.Submenu).filter(models.Submenu.id == target_submenu_id).first()
    return submenu


def get_submenus(target_menu_id: uuid.UUID, db: Session):
    menu = db.query(models.Menu).filter(models.Menu.id == target_menu_id).first()
    if menu is None:
        return []
    return menu.submenus


def create_submenu(target_menu_id: uuid.UUID, db: Session, submenu: schemas.SubmenuIn):
    menu = db.query(models.Menu).filter(models.Menu.id == target_menu_id).first()
    if menu is None:
        return None
    db_submenu = models.Submenu(title=submenu.title,
                                description=submenu.description,
                                menu_id=target_menu_id)
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return get_submenu(target_submenu_id=db_submenu.id, db=db, target_menu_id=target_menu_id)


def update_submenu(target_menu_id: uuid.UUID, target_submenu_id: uuid.UUID, submenu: schemas.SubmenuIn, db: Session):
    db.query(models.Submenu).filter(models.Submenu.id == target_submenu_id).update(
        {'title': submenu.title, 'description': submenu.description})
    db.commit()
    return get_submenu(target_submenu_id=target_submenu_id, db=db, target_menu_id=target_menu_id)


def delete_submenu(target_submenu_id: uuid.UUID, db: Session):
    submenu = db.query(models.Submenu).get(target_submenu_id)
    if submenu:
        db.delete(submenu)
        db.commit()
    return get_menu(target_menu_id=target_submenu_id, db=db)


def get_dish(db: Session, target_dish_id: uuid.UUID):
    dish = db.query(models.Dish).filter(models.Dish.id == target_dish_id).first()
    return dish


def get_dishes(target_submenu_id: uuid.UUID, db: Session):
    dishes = db.query(models.Submenu).filter(models.Submenu.id == target_submenu_id).first()
    if dishes is None:
        return []
    return dishes.dishes


def create_dish(target_submenu_id: uuid.UUID, db: Session, dish: schemas.DishIn):
    db_dish = models.Dish(title=dish.title,
                          description=dish.description,
                          price=dish.price,
                          submenu_id=target_submenu_id)
    db.add(db_dish)
    db.commit()
    db.refresh(db_dish)
    return get_dish(db=db, target_dish_id=db_dish.id)


def update_dish(target_dish_id: uuid.UUID, dish: schemas.DishIn, db: Session):
    db.query(models.Dish).filter(models.Dish.id == target_dish_id).update(
        {'title': dish.title, 'description': dish.description, 'price': dish.price})
    db.commit()
    return get_dish(target_dish_id=target_dish_id, db=db)


def delete_dish(target_dish_id: uuid.UUID, db: Session):
    dish = db.query(models.Dish).get(target_dish_id)
    if dish:
        db.delete(dish)
        db.commit()
    return get_menu(target_menu_id=target_dish_id, db=db)
