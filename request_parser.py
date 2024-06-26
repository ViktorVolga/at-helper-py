import abc

class RequestParser(abc.ABC):
    m_at = None
    m_answer = None
    def __init__(self, at, answer):
        self.m_at = at
        self.m_answer = answer
    @abc.abstractmethod
    def parse(self): pass
    
    


