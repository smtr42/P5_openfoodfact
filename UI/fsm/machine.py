from .my_states import StartMenu, ProductMenu
import os
import time
import sys


class Machine(object):
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = StartMenu()
        self.start_menu = self.state
        self.back_menu = None
        self.product_menu = None

    def show(self):
        self.state.show()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
        # The next state will be the result of the on_event function.
        if self.state != self.back_menu:
            self.back_menu = self.state
        self.state = self.state.on_event(event)

    def input_checker(self):
        input_error_message = \
            ("\n"
             "!! write down one of the number on the screen !!"
             "\n")

        while True:
            ui = input(
                """Choose the menu you want to access by writing the line's 
number : Go back is 'r', quit is 'q' \n => """)
            try:
                ui = int(ui)
            except ValueError:
                if ui == "q":
                    self.exit_program()
                elif ui == "r":
                    self.go_back()
                    return "bck"
                elif ui == "m":
                    self.go_start()
                    return "strtmnu"
                elif ui == "fav" and self.state == ProductMenu:
                    return "add_fav"
                else:
                    print(input_error_message)
                    self.show()
                    continue
            if ui > max(self.state.menu.keys()):
                print(input_error_message)
                self.show()
            elif ui <= 0:
                print(input_error_message)
                self.show()
            else:
                return ui

    def exit_program(self):
        i = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print(  "The program will quit in ", i, "s"
                "\n"
                "Your favorites are permanently saved in the database"
                "\n"
                "Thanks for using this program !")
        while i >= 0:
            print(i, "s")
            time.sleep(1)
            i -= 1
        sys.exit()

    def go_back(self):

        self.state = self.back_menu

    def go_start(self):
        self.state = self.start_menu
