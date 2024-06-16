import atrequest

class CSQ(atrequest.ATRequest):
    def __init__(self):
        super().__init__(b'AT+CSQ\r', 100, 'quality of connection', False)             

