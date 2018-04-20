import time
import uuid


class Transaction:

    def __init__(self, payload):
        self.id = uuid.uuid1()
        self.payload = payload
        self.timestamp = int(time.time())
        self.confirmed = False
