import io_port
import module

class OneThreadIOService(module.Module):
    primary_port = io_port.IOPort("/dev/ttyUSB2", 115200)
    secondary_port = io_port.IOPort("/dev/ttyUSB1", 115200)
    connected = False

    def __init__(self, director):
        super().__init__(director)
        self.secondary_port.open()
    
    def exec_request(self, request):
        if self.connected:
            self.secondary_port.write(request.command)
            return self.secondary_port.read(request.max_lead_time)
        else:
            self.primary_port.write(request.command)
            return self.secondary_port.read(request.max_lead_time)
        
    def notify(self, message):
        if 'connected' in message:
            self.connected = True
        elif 'disconnected' in message:
            self.connected = False

