from hashlib import sha256
from pprint import pprint
import json
import time
import collections


ENCODING = "utf-8"

class Block:
    """
    represents a single block of the chain
    """
    def __init__(self, index, previousBlockHash, timestamp = None):
        if timestamp is None:
            timestamp = int(time.time())
        self.index = index
        self.previousBlockHash = previousBlockHash
        self.timestamp = timestamp
        self.transactions = []
        self.proof = 0

    def set_proof(self, proof):
        self.proof = proof

    def add_transaction(self, id, timestamp, payload):
        self.transactions.append({"id": id, "timestamp" : timestamp, "payload": payload})

    def to_ordered_dict(self):
        dict = collections.OrderedDict()
        dict["index"] = self.index
        dict["timestamp"] = self.timestamp
        dict["proof"] = self.proof
        dict["transactions"] = self.transactions
        dict["previousBlockHash"] = self.previousBlockHash
        return dict
