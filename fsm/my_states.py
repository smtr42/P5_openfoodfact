# my_states.py

from state import State


# Start of our states
class StartMenu(State):
    """
    The state which indicates that there are limited device capabilities.
    """

    def show(self):
        print("1. => Quel aliment souhaitez-vous remplacer ?\n"
              "2. Retrouver mes aliments substitués\n"
              "3. Quitter")

    def on_event(self, event):
        if event == 1:
            return CategoryMenu()
        if event == 2:
            return FavMenu()
        if event == 3:
            return LoopStopper()
        return self


class CategoryMenu(State):
    """
    The state which indicates that there are no limitations on device
    capabilities.
    """

    def __init__(self):
        self.cat_list = self.get_random_cat()

    def show(self):
        for item in self.cat_list:
            print(f"{item}. {self.cat_list[item]}")

    def on_event(self, event):
        if event in self.cat_list.keys():
            return ProductMenu(self.cat_list[event])
        if event == 6:
            return StartMenu()
        return self

    def get_random_cat(self):
        # aller récupérer la fonction dans le manager
        cat_list = {1: "fromage", 2: "vin", 3: "pizza", 4: "snack", 5: "soda"}
        return cat_list


class ProductMenu(State):
    def __init__(self, selected_cat):
        self.selected_cat = selected_cat
        self.prod_list = self.get_product_by_category()

    def show(self):
        for item in self.prod_list:
            print(f"{item}. {self.prod_list[item]}")

    def on_event(self, event):
        return
        pass

    def get_product_by_category(self):
        # aller récupérer la fonction dans le manager en fonction cate
        prod_list = {1: "camembert", 2: "vieux pané", 3: "st felicien",
                     4: "gruyère", 5: "morbier"}
        return prod_list

class ShowProduct(State):

    def show(self):
        pass

    def on_event(self):
        # affichage du produit
        # possibilité de sauvegarder
        # possibilité de quitter
        pass

    def get_product_data(self):
        # à récupérer dans le manager
        pass

    def save_product_into_fav(self):
        # à récupérer dans le manager
        pass

class FavMenu(State):
    pass


class LoopStopper(State):
    def on_event(self, event):
        pass

# End of our states.
