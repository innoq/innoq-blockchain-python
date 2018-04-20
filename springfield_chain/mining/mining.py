from springfield_chain.block.blocks import block_from_dict
from springfield_chain.hashing import hash_api
import subprocess

from springfield_chain.block.blocks import Block

def is_proven_hash(hash):
    return hash.startswith('0000')

def check_block(block):
    h = hash_api.hash_block(block)
    return is_proven_hash(h)

def mine_proof(block, proof=0, n=10000000):
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