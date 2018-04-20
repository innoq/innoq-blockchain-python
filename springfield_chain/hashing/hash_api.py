from hashlib import sha256
import json

ENCODING = "utf-8"

def hash_block(block):
    """ expects a block object """
    block_as_json = json.dumps(block.to_ordered_dict(), separators=(",", ":"), sort_keys=False)
    return sha256(block_as_json.encode(ENCODING)).hexdigest()


def hash_block_with_proof(block, proof):
    block.proof = proof
    return hash_block(block)
