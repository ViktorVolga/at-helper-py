import module

class LedsController(module.Module):
    def __init__(self, director):
        super().__init__(director)

    def notify(self, message):
        print("[LedsController] accept message {}", message)