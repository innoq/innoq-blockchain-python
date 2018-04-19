from springfield_chain.block.blocks import block_from_dict
from springfield_chain.hashing import hash_api

def is_proven_hash(hash):
    return hash.startswith('0000')

def check_block(block_dict):
    block = block_from_dict(block_dict)
    h = hash_api.hash_block(block)
    return is_proven_hash(h)

def mine_block(block_dict, proof=0, n=10000000):
    block = block_from_dict(block_dict)
    for p in range(proof, proof + n):
        h = hash_api.hash_block_with_proof(block, p)
        if is_proven_hash(h):
            block.set_proof(p)
            return block

def mine_block_parallel(block):
    mine_block(block)