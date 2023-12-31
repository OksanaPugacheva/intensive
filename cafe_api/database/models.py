import uuid

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menus'

    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)
    title = Column(String)
    description = Column(String)
    submenus = relationship('Submenu', back_populates='menu', cascade='all, delete-orphan')


class Submenu(Base):
    __tablename__ = 'submenus'

    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)
    menu_id = Column(UUID(as_uuid=True), ForeignKey('menus.id'))
    title = Column(String)
    description = Column(String)
    dishes = relationship('Dish', back_populates='submenu', cascade='all, delete-orphan')
    menu = relationship('Menu', back_populates='submenus')


class Dish(Base):
    __tablename__ = 'dishes'

    id = Column(UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey('submenus.id'))
    title = Column(String)
    description = Column(String)
    price = Column(String)
    submenu = relationship('Submenu', back_populates='dishes')
