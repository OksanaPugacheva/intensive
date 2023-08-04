from uuid import UUID

from pydantic import BaseModel


class MenuIn(BaseModel):
    title: str
    description: str


class MenuOut(BaseModel):
    id: UUID
    title: str
    description: str
    submenus_count: int
    dishes_count: int


class SubmenuIn(BaseModel):
    title: str
    description: str


class SubmenuOut(BaseModel):
    id: UUID
    title: str
    description: str
    dishes_count: int


class SomethingDelete(BaseModel):
    status: bool
    detail: str


class DishIn(BaseModel):
    title: str
    description: str
    price: float


class DishOut(BaseModel):
    id: UUID
    title: str
    description: str
    price: str
