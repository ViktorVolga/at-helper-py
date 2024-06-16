import abc
import logger
import io_service

class Director(abc.ABC):    
    @abc.abstractmethod
    def send(self, message, module): pass

class ModemDirector(Director):
    io = None
    def send(self, message, module):
        print(message)
        if module == self.io:
            print("sender io")
    def __init__(self):
        self.io = io_service.IOService(self)

    def test(self):
        self.io.notify("hello from director")