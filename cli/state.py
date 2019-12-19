class State:

    def __init__(self):
        print("processing current State", str(self))

    def on_event(self, event):
        """
        Handle events that are delegated to this state
        """
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
