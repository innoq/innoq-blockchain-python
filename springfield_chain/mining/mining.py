
from springfield_chain.hashing import hash_api

HASH_PREFIX = '0000'

from springfield_chain.block.blocks import Block

def is_proven_hash(hash):
    return hash.startswith(HASH_PREFIX)

def check_block(block):
    if not block.is_valid():
        return False
    h = hash_api.hash_block(block)
    return is_proven_hash(h)

def mine_block(block, proof=0, n=10000000):
    if not block.is_valid():
        raise ValueError('this block is not valid')
    for p in range(proof, proof + n):
        h = hash_api.hash_block_with_proof(block, p)
        if is_proven_hash(h):
            return p
        else:
            p += 1
    return None

def mine_block (last_block):

    last_hash = hash_api.hash_block(last_block)
    print(str(last_block))
    new_block = Block(last_block.index + 1, last_hash)
    proof = mine_proof(new_block)
    new_block.set_proof(proof)
    return new_block

#def mine_block_parallel(block):
 #   subprocess
  #  mine_block(block)