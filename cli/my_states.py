from cli.state import State


class LockedState(State):

    def on_event(self, event):
        if event == "pin_entered":
            return UnlockedState()


class UnlockedState(State):
    def on_event(self, event):
        if event == "device_locked":
            return LockedState()
        return self

