from hashlib import sha256
from pprint import pprint
import json
import time
import collections


ENCODING = "utf-8"
MAX_TX = 5

class Block:
    """
    represents a single block of the chain
    """
    def __init__(self, index, previousBlockHash, timestamp = None, proof = 0):
        if timestamp is None:
            timestamp = int(time.time())
        self.index = index
        self.previousBlockHash = previousBlockHash
        self.timestamp = timestamp
        self.transactions = []
        self.proof = proof

    def set_proof(self, proof):
        self.proof = proof

    def add_transaction(self, new_tx):
        self.transactions.append(new_tx)

    def add_transaction_singleparams(self, id, timestamp, payload):
        new_tx = collections.OrderedDict([('id', id), ('timestamp', timestamp), ('payload', payload)])
        self.transactions.append(new_tx)

    def is_valid(self):
        if (len(self.transactions) < MAX_TX):
            return True
        else:
            return False

    def to_ordered_dict(self):
        dict = collections.OrderedDict()
        dict["index"] = self.index
        dict["timestamp"] = self.timestamp
        dict["proof"] = self.proof
        dict["transactions"] = self.transactions
        dict["previousBlockHash"] = self.previousBlockHash
        return dict

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def block_from_dict(data):
    if type(data) == Block:
        return data
    block = Block(data["index"], data["previousBlockHash"], data["timestamp"], data["proof"])
    for tx in data["transactions"]:
        block.add_transaction_singleparams(tx["id"], tx["timestamp"], tx["payload"])
    return block

