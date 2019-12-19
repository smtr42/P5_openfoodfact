from cli.my_states import LockedState


class SimpleDevice:
    def __init__(self):
        self.state = LockedState()

    def on_event(self, event):
        self.state = self.state.on_event(event)

print("test")
device = SimpleDevice()
