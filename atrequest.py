import abc

class ATRequest(abc.ABC):
    command = None
    max_lead_time = None
    description = None
    complited = False

    def __init__ (self, request, max_lead_time = None, description = None):
        self.request = request
        self.max_lead_time = max_lead_time
        self.description = description
