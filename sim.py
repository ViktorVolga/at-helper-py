import module

class SimController(module.Module):
    def __init__(self, director):
        super().__init__(director)

    def notify(self, message):
        print("[Sim] accept message {}", message)