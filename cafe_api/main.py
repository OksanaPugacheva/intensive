from uuid import UUID

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from cafe_api import answer, crud, models, schemas
from cafe_api.database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def homepage():
    return {"detail": "All right"}


@app.post("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes", status_code=201)
def create_dish(target_submenu_id: UUID, dish: schemas.DishIn, db: Session = Depends(get_db)):
    new_dish = crud.create_dish(db=db, target_submenu_id=target_submenu_id, dish=dish)
    return answer.dish_answer(new_dish)


@app.post("/api/v1/menus/{target_menu_id}/submenus", status_code=201)
def create_submenu(target_menu_id: UUID, submenu: schemas.SubmenuIn, db: Session = Depends(get_db)):
    new_submenu = crud.create_submenu(db=db, submenu=submenu, target_menu_id=target_menu_id)
    if new_submenu is None:
        return answer.submenu_nf
    return answer.submenu_answer(new_submenu)


@app.post("/api/v1/menus", response_model=schemas.MenuOut, status_code=201)
def create_menu(menu: schemas.MenuIn, db: Session = Depends(get_db)):
    menu = crud.create_menu(db=db, menu=menu)
    return answer.menu_answer(menu)


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
def get_dish(target_dish_id: UUID, db: Session = Depends(get_db)):
    dish = crud.get_dish(db=db, target_dish_id=target_dish_id)
    if dish is None:
        return answer.dish_nf
    return answer.dish_answer(dish)


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes")
def get_dishes(target_submenu_id: UUID, db: Session = Depends(get_db)):
    dishes = crud.get_dishes(target_submenu_id=target_submenu_id, db=db)
    return dishes


@app.get("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
def get_submenu(target_menu_id: UUID, target_submenu_id: UUID, db: Session = Depends(get_db)):
    submenu = crud.get_submenu(target_submenu_id=target_submenu_id, db=db, target_menu_id=target_menu_id)
    if submenu is None:
        return answer.submenu_nf
    return answer.submenu_answer(submenu)


@app.get("/api/v1/menus/{target_menu_id}/submenus")
def get_submenus(target_menu_id: UUID, db: Session = Depends(get_db)):
    submenu = crud.get_submenus(target_menu_id=target_menu_id, db=db)
    submenus_list = list()
    for submenu in submenu:
        submenus_list.append(answer.submenu_answer(submenu))
    return submenus_list


@app.get("/api/v1/menus/{target_menu_id}", response_model=schemas.MenuOut, status_code=200)
def get_menu(target_menu_id: UUID, db: Session = Depends(get_db)):
    menu = crud.get_menu(db=db, target_menu_id=target_menu_id)
    if menu is None:
        return answer.menu_nf
    return answer.menu_answer(menu)


@app.get("/api/v1/menus", status_code=200)
def get_menus(db: Session = Depends(get_db)):
    menus = list()
    for menu in crud.get_menus(db=db):
        menus.append(answer.menu_answer(menu))
    return menus


@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}")
def update_dish(target_dish_id: UUID, dish: schemas.DishIn, db: Session = Depends(get_db)):
    upd_dish = crud.update_dish(target_dish_id=target_dish_id, db=db, dish=dish)
    if upd_dish is None:
        return answer.dish_nf
    return answer.dish_answer(upd_dish)


@app.patch("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}")
def update_submenu(target_menu_id: UUID, target_submenu_id: UUID, submenu: schemas.SubmenuIn,
                   db: Session = Depends(get_db)):
    upd_submenu = crud.update_submenu(target_submenu_id=target_submenu_id, submenu=submenu, db=db,
                                      target_menu_id=target_menu_id)
    if upd_submenu is None:
        return answer.menu_nf
    return answer.submenu_answer(upd_submenu)


@app.patch("/api/v1/menus/{target_menu_id}")
def update_menu(target_menu_id: UUID, menu: schemas.MenuIn, db: Session = Depends(get_db)):
    upd_menu = crud.update_menu(db=db, menu=menu, target_menu_id=target_menu_id)
    if upd_menu is None:
        return answer.menu_nf
    return answer.menu_answer(upd_menu)


@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}/dishes/{target_dish_id}",
            response_model=schemas.SomethingDelete)
def delete_dish(target_dish_id: UUID, db: Session = Depends(get_db)):
    dish = crud.delete_dish(target_dish_id=target_dish_id, db=db)
    if dish is None:
        return {"status": True, "detail": "The dish has been deleted"}
    else:
        return {"status": False, "detail": "The dish hasn't been deleted"}


@app.delete("/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}", response_model=schemas.SomethingDelete)
def delete_submenu(target_menu_id: UUID, target_submenu_id: UUID, db: Session = Depends(get_db)):
    submenu = crud.delete_submenu(target_submenu_id=target_submenu_id, db=db)
    if target_menu_id:
        if submenu is None:
            return {"status": True, "detail": "The submenu has been deleted"}
        else:
            return {"status": False, "detail": "The submenu hasn't been deleted"}


@app.delete("/api/v1/menus/{api_test_menu_id}", response_model=schemas.SomethingDelete)
def delete_menu(api_test_menu_id: UUID, db: Session = Depends(get_db)):
    menu = crud.delete_menu(target_menu_id=api_test_menu_id, db=db)
    if menu is None:
        return {"status": True, "detail": "The menu has been deleted"}
    else:
        return {"status": False, "detail": "The menu hasn't been deleted"}


def start_uvicorn():
    uvicorn.run("cafe_api.main:app",
                host="0.0.0.0",
                port=5000,
                reload=True)
