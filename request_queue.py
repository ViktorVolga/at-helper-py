import threading
import logger


'''
    blocking queue. If queue empty - block process until nofing to read from queue   
'''   
class BlockingRequestQueue:
    queue = []
    condition = None
    log = None

    def __init__(self):
        self.condition = threading.Condition()
        self.log = logger.Logger(__name__)
        self.log.logger.debug("[BlockingRequestQueue] - constructor - ok")

    def add_request(self, request):
        if not request:
            self.log.logger.error("[BlockingRequestQueue] request empty")
            return
        
        with self.condition:
            self.queue.append(request)
            self.condition.notify(1)
            self.log.logger.debug("[BlockingRequestQueue] new request adde to queue")

    def get_request(self):
        with self.condition:            
            while len(self.queue) <= 0:
                self.log.logger.debug("[BlockingRequestQueue] no request in queue - wait request")
                self.condition.wait()
            request = self.queue.pop(0)
        self.log.logger.debug("[BlockingRequestQueue] returned one request")
        return request

'''
    queue for polling. 
    return None if empty
'''   
class NonBlockRequestQueue:
    queue = []    
    log = None
    lock = None

    def __init__(self):
        self.log = logger.Logger(__name__)        
        self.lock = threading.Lock()
        self.log.logger.debug("[NonBlockRequestQueue] - constructor - ok")

    def add_request(self, request):
        if not request:
            self.log.logger.error("[NonBlockRequestQueue] request empty")
            return
        
        self.lock.acquire()
        try:
            self.queue.append(request)
            self.log.logger.debug("[NonBlockRequestQueue] - put one request to queue")
        finally:
            self.lock.release()

    def get_request(self):
        self.lock.acquire()
        try:
            if len(self.queue) > 0:
                self.log.logger.debug("[NonBlockRequestQueue] - put one request to queue")
                return self.queue.pop(0)
            else:
                self.log.logger.debug("[NonBlockRequestQueue] - queue is empty")
        finally:
            self.lock.release()

        






    