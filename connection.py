import module

class ConnectionController(module.Module):
    def __init__(self, director):
        super().__init__(director)

    def notify(self, message):
        print("[ConnectionController] accept message {}", message)