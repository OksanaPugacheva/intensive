from sqlalchemy import Column, String, Float, ForeignKey, UUID
from sqlalchemy.orm import relationship
from database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True)
    title = Column(String)
    description = Column(String)
    submenus = relationship("Submenu", back_populates="menu", cascade="all, delete-orphan")


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True)
    menu_id = Column(UUID(as_uuid=True), ForeignKey("menus.id"))
    title = Column(String)
    description = Column(String)
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete-orphan")
    menu = relationship("Menu", back_populates="submenus")


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(UUID(as_uuid=True), nullable=False, unique=True, primary_key=True)
    submenu_id = Column(UUID(as_uuid=True), ForeignKey("submenus.id"))
    title = Column(String)
    description = Column(String)
    price = Column(Float)
    submenu = relationship("Submenu", back_populates="dishes")
