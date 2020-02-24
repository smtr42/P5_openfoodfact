from .state import State
# import dbmanagement.main_manager as manager
from dbmanagement.manager.product_manager import product_manager

class StartMenu(State):
    def __init__(self):
        self.menu = {
            1: CategoryMenu,
            2: FavMenu,
        }

    def show(self):
        print("\n"
              "1. Search for food you which to substitute\n"
              "2. Find my saved favorites healthy food\n")

    def on_event(self, event):
        if event == "strtmnu":
            return self
        else:
            return self.menu.get(event, lambda: "")()


class CategoryMenu(State):

    def __init__(self):
        self.menu = self.get_random_cat()

    def show(self):
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")

    def on_event(self, event):
        if event == "bck":
            return self
        elif event in self.menu.keys():
            return ProductMenu(self.menu[event])
        return self

    def get_random_cat(self):
        # aller récupérer la fonction dans le manager
        cat_list = {1: "Fromages", 2: "Desserts", 3: "Viandes", 4: "Chocolats", 5: "####"}
        return cat_list


class ProductMenu(State):
    def __init__(self, selected_cat):
        self.selected_cat = selected_cat
        self.menu = self.get_product_by_category()

    def show(self):
        for item in self.menu:
            print(f"{item}. {self.menu[item]}")

    def on_event(self, event):
        if event == "bck":
            return self
        elif event in self.menu.keys():
            return SubProductMenu(self.menu[event], self.selected_cat)
        return self

    def get_product_by_category(self):
        category = self.selected_cat
        prod_list = product_manager.get_unhealthy_prod_by_category(
            category)
        return prod_list


class SubProductMenu(State):
    def __init__(self, selected_prod, selected_cat):
        self.selected_prod = selected_prod
        self.selected_cat = selected_cat
        self.menu = self.get_healthier_product()

    def show(self):
        print("Here is a list of much better food than the one you selected")
        for item in self.menu[0]:
            print(f"{item}. {self.menu[0][item]}")
        print("\n "
              "Write a number to see the detail of the product")

    def on_event(self, event):
        if event == "fav":
            return self
        elif event in self.menu.keys():
            return ShowProduct(self.menu[event], self.selected_prod,
                               self.selected_cat)

        # possibilité de sauvegarder
        # possibilité de voir les fav
        pass

    def get_healthier_product(self):

        prod_list = product_manager.get_healthier_product_by_category(
            self.selected_cat)
        return prod_list
        pass


class ShowProduct(State):
    def __init__(self, event, prod, cat):
        self.event = event
        self.product_name = prod
        self.cat = cat

    def show(self):

        pass

    def on_event(self, event):
        pass

    def get_product(self):
        product = {}
        product_manager.get_product_by_name(self.product_name)
        return product
        pass

    def save_product_into_fav(self):
        # à récupérer dans le manager
        main_manager.product_manager.save_healthy_product_to_favory()
        pass


class FavMenu(State):
    def __init__(self):
        # get list of fav
        pass

    def show(self):
        # show the menu with the list
        pass

    def on_event(self, event):
        # select number and go to state
        pass

    def get_fav(self):
        # get fav from database
        pass

# End of our states.
