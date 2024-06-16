import logging

class Logger:
    logger = None
    def __init__ (self, file):
        self.logger = logging.getLogger(file)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler("/tmp/at-helper.log", mode ='w')
        formatter = logging.Formatter("[%(name)s] [%(asctime)s] [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)   
