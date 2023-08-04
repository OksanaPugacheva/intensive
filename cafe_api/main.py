import uvicorn
from fastapi import FastAPI

from cafe_api.routers import dish_router, menu_router, submenu_router

app = FastAPI()
app.include_router(menu_router.router, prefix='/api/v1', tags=['menu'])
app.include_router(submenu_router.router, prefix='/api/v1/menus/{target_menu_id}', tags=['submenu'])
app.include_router(dish_router.router, prefix='/api/v1/menus/{target_menu_id}/submenus/{target_submenu_id}',
                   tags=['dish'])


@app.get('/')
def homepage():
    return {'detail': 'All right'}


def start_uvicorn():
    uvicorn.run('cafe_api.main:app',
                # host="0.0.0.0",
                port=8000,
                reload=True)
