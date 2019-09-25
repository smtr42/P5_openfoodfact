from . import managers
from .database import db
from dataclasses import dataclass


@dataclass
class Product:

    # objects = managers.ProductManager(db)

    barcode: int = None
    product_name: str = None
    description: str = None
    # nutrigrade: int = None
    nutriscore: str = None
    url: str = None


@dataclass
class Store:
    id: int = None
    store_name: str = None


@dataclass
class Category:
    id: int = None
    category_name: str = None


@dataclass
class Favorite:
    id: int = None
    product_barcode: int = None
    substitute_barcode: int = None


if __name__ == "__main__":
    product = Product.objects.get_healthier_than()
