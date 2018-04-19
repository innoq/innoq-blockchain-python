from hashlib import sha256
import json
from springfield_chain.block.blocks import Block, block_from_dict

ENCODING = "utf-8"

def hashBlock(data):
    return hashBlockWithProof(data, data["proof"])

def hashBlockWithProof(data, proof):
    block = block_from_dict(data)
    block.proof = proof
    block_as_json = json.dumps(block.to_ordered_dict(), separators=(",", ":"), sort_keys=False)
    return sha256(block_as_json.encode(ENCODING)).hexdigest()
