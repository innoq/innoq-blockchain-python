from hashlib import sha256
import json
from springfield_chain.block.blocks import Block

ENCODING = "utf-8"

def hashBlock(data):
    return hashBlockWithProof(data, data["proof"])

def hashBlockWithProof(data, proof):
    block = Block(data["index"], data["previousBlockHash"], data["timestamp"])
    for tx in data["transactions"]:
        block.add_transaction(tx["id"], tx["timestamp"], tx["payload"])
    block.proof = proof
    block_as_json = json.dumps(block.to_ordered_dict(), separators=(",", ":"), sort_keys=False)
    hash = sha256(block_as_json.encode(ENCODING)).hexdigest()
    return hash
