import colorful as cf

from dbmanagement.manager.category_manager import CategoryManager
from dbmanagement.manager.favorite_manager import favorite_manager
# import dbmanagement.main_manager as manager
from dbmanagement.manager.product_manager import product_manager
from .state import State


class StartMenu(State):
    """The first State with the main menu. Two options are possibles."""

    def __init__(self):
        self.menu = {
            1: CategoryMenu,
            2: FavMenu,
        }

    def show(self):
        print("\n \n"
              "1. Search for food you which to substitute\n"
              "2. Find my saved favorites healthy food\n")

    def on_event(self, event):
        if event in ("strtmnu", "bck", "r", "add_fav"):
            return StartMenu()
        else:
            return self.menu.get(event, lambda: "")()


class CategoryMenu(State):
    """The follow up state after selecting the first menu. Now selecting which
    category to choose"""

    def __init__(self):
        self.menu = self.get_random_cat()

    def show(self):
        print("\n \n")
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")

    def on_event(self, event):
        if event == "bck":
            return self
        elif event in self.menu.keys():
            return ProductMenu(self.menu[event])
        return self

    def get_random_cat(self):
        cat_list = CategoryManager.get_cat()
        return cat_list


class ProductMenu(State):
    """State where the user select an unhealthy product from selected category
    in precedent state"""

    def __init__(self, selected_cat):
        self.uh_barcode = {}
        self.temp = {}
        self.selected_cat = selected_cat
        self.menu = self.get_product_by_category()

    def show(self):
        print("\n \n")
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")

    def on_event(self, event):
        if event == "bck":
            return self
        elif event in self.menu.keys():
            return SubProductMenu(
                self.menu[event], self.selected_cat, self.uh_barcode)
        return self

    def get_product_by_category(self):
        prod_list = product_manager.get_unhealthy_prod_by_category(
            self.selected_cat)
        for enum, (barcode, name) in enumerate(prod_list.items()):
            enum += 1
            self.uh_barcode[enum] = barcode
            self.temp[enum] = name
        return self.temp


class SubProductMenu(State):
    """State where the substitute product list is displayed in regards of
    selected category and unhealthy product"""

    def __init__(self, selected_prod, selected_cat, uh_barcode):
        self.uh_barcode = uh_barcode
        self.selected_prod = selected_prod
        self.selected_cat = selected_cat
        self.barcode = {}
        self.temp = {}
        self.menu = self.get_healthier_product()

    def show(self):
        print("\n \n \n"
              "Here is a list of much better food than the one you selected")
        # for enum, (barcode, name) in enumerate(self.menu.items()):
        #     print(f"{enum}. {self.menu[barcode]}")
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")
        print("\n "
              "Write a number to see the detail of the product")

    def on_event(self, event):
        if event in self.menu.keys():
            return ShowProduct(event, self.barcode[event], self.selected_prod,
                               self.selected_cat, self.uh_barcode)
        else:
            return self

    def get_healthier_product(self):

        prod_list = product_manager.get_healthier_product_by_category(
            self.selected_cat)
        for enum, (barcode, name) in enumerate(prod_list.items()):
            enum += 1
            self.barcode[enum] = barcode
            self.temp[enum] = name
        return self.temp


class ShowProduct(State):
    """State where the description of the selected substitued product
    is diplayed, with the option to save it"""

    def __init__(self, event, barcode, prod, cat, uh_barcode):
        self.uh_barcode = uh_barcode
        self.barcode = barcode
        self.event = event
        self.product_name = prod
        self.category = cat
        self.full_product = self.get_product()

    def show(self):
        print(f"\n \n \n"
              f"{self.full_product['product_name']} is a better food as it has"
              f" a nutriscore graded {self.full_product['nutriscore']}."
              f"\n You can buy it in these stores : "
              f"{self.full_product['store_name']}"
              f"\n For more information visit this url : "
              f"{self.full_product['url']}")
        print(cf.white("\n If you want to " + cf.red('save', nested=True) +
                       " this food into your favorite, "
                       + cf.red('press "s" ', nested=True) + "\n \n \n"))

    def on_event(self, event):
        if event == "add_fav":
            self.save_product_into_fav()
            return StartMenu()
        elif event == "bck":
            return SubProductMenu(
                self.product_name, self.category, self.uh_barcode)

    def get_product(self):
        product = product_manager.get_product_by_barcode(self.barcode)
        return product

    def save_product_into_fav(self):
        favorite_manager.save_healthy_product_to_favorite(self.event,
                                                          self.uh_barcode,
                                                          self.full_product)
        print("Your favorite substitute have been saved")


class FavMenu(State):
    """The Sate where you can access the list of favorites products"""

    def __init__(self):
        self.fav_name = {}
        self.fav_barcode = {}
        self.menu = self.get_fav_by_barcode()

    def show(self):
        print("\n \n")
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")
        pass

    def on_event(self, event):
        if event == "bck":
            return StartMenu()
        else:
            return ShowFavProduct(event, self.fav_barcode[event])

    def get_fav_by_barcode(self):
        self.fav_name, self.fav_barcode = favorite_manager.get_all_favorite()
        return self.fav_name

    def get_product(self):
        pass


class ShowFavProduct(State):
    def __init__(self, event, barcode):
        self.event = event
        self.barcode = barcode
        self.full_product = self.get_product()

    def show(self):
        print(f"\n \n \n"
              f"{self.full_product['product_name']} is a better food as it has"
              f" a nutriscore graded {self.full_product['nutriscore']}."
              f"\n You can buy it in these stores : "
              f"{self.full_product['store_name']}"
              f"\n For more information visit this url : "
              f"{self.full_product['url']}")

    def event(self, event):
        if event == "bck":
            return FavMenu()
        else:
            return ShowFavProduct(event, self.fav_barcode[event])
        pass

    def get_product(self):
        product = product_manager.get_product_by_barcode(self.barcode)
        return product
