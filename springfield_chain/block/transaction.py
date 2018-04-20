import time
import uuid


class Transaction:

    def __init__(self, payload):
        self.id = uuid.uuid1()
        self.timestamp = int(time.time())
        self.payload = str.replace(payload, " ", "") #clear out whitespaces
        self.confirmed = False
