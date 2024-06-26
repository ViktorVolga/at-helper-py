import abc

class Module(abc.ABC):
    director = None
    def __init__(self, director):
        self.director = director
    @abc.abstractmethod
    def notify(self, message): pass
    def send(self, message):
        self.director.send(message, self)