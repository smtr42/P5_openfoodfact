# my_states.py
from .state import State
import dbmanagement.main_manager as manager


class StartMenu(State):
    def __init__(self):
        super().__init__()
        self.menu = {
            1: CategoryMenu,
            2: FavMenu,
        }

    def show(self):
        print("1. Search for food you wich to substitute\n"
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
        cat_list = {1: "fromage", 2: "vin", 3: "pizza", 4: "snack", 5: "soda"}
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
        return self

    def get_product_by_category(self):
        a = manager
        # aller récupérer la fonction dans le manager en fonction category
        prod_list = {1: "camembert", 2: "vieux pané", 3: "st felicien",
                     4: "gruyère", 5: "morbier"}
        return prod_list


class ShowProduct(State):

    def show(self):
        print("Description of item you selected :")
        # affichage du produit
        print("To add this item to you favorite write exactly down 'fav' \n"
              "To go back to the precedent menu write 'r'")
        pass

    def on_event(self, event):
        if event == "add_fav":
            # function add product to favorite
            pass
        # possibilité de sauvegarder
        # possibilité de voir les fav
        pass

    def get_product_data(self):
        # à récupérer dans le manager
        pass

    def save_product_into_fav(self):
        # à récupérer dans le manager
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
