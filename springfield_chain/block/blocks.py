from hashlib import sha256
from pprint import pprint
import json

ENCODING = "utf-8"

def hashBlock(block):
    block_as_json = json.dumps(block, separators=(",", ":"), sort_keys=True)
    hash = sha256(block_as_json.encode(ENCODING)).hexdigest()
    return hash


def hashBlockWithProof(block, proof):
    block["proof"] = proof
    return hashBlock(block)
