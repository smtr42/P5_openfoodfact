from my_states import StartMenu


class Machine(object):
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self):
        """ Initialize the components. """

        # Start with a default state.
        self.state = StartMenu()

    def show(self):
        self.state.show()

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

    def input_checker(self):
        while True:
            ui = input("Write a number :")
            try:
                ui = int(ui)
            except ValueError:
                print("Entrer UNIQUEMENT un chiffre")
                continue
            if ui > 6:
                print("Entrer UNIQUEMENT un chiffre comme affiché")
            elif ui <= 0:
                print("Entrer UNIQUEMENT un chiffre comme affiché")
            else:
                return ui
