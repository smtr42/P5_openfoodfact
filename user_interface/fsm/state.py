class State(object):
    """Define object which provides utility functions for the
    individual states in the state machine."""

    def show(self):
        """Handle printing function for this state"""
        pass

    def on_event(self, event):
        """Handle events that are delegated to this State."""
        pass

