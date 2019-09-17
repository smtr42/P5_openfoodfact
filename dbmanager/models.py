from . import managers
from .database import db
from dataclasses import dataclass


@dataclass
class Product:

    objects = managers.ProductManager(db)

    barcode: int = None
    description: str = None
    nutrigrade: int = None
    nutriscore: str = None
    url: str = None


@dataclass
class Store:
    id: int = None
    store_name: str = None


@dataclass
class Category:
    category_name: str = None


@dataclass
class Favorite:
    id: int = None
    product_name: str = None
    substitute_name: str = None


if __name__ == "__main__":
    product = Product.objects.get_healthier_than()
