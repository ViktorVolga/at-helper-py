import abc
import logger
import io_service
import sim
import connection
import leds

class Director(abc.ABC):    
    @abc.abstractmethod
    def send(self, message, module): pass

class ModemDirector(Director):
    io = None
    sim = None
    connection = None
    leds = None

    def send(self, message, module):
        print(message)
        if module == self.io:
            print("sender io")

    def __init__(self):
        self.io = io_service.IOService(self)
        self.sim = sim.SimController(self)
        self.connection = connection.ConnectionController(self)
        self.leds = leds.LedsController(self)

    def test(self):
        self.io.notify("hello from director")
        self.sim.notify("hello from director")
        self.connection.notify("hello from director")
        self.leds.notify("hello from director")