import time
import uuid
import json

class Transaction:

    def __init__(self, payload):
        self.id = uuid.uuid1()
        self.payload = payload
        self.timestamp = int(time.time())
        self.confirmed = False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
