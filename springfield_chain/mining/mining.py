
from springfield_chain.hashing import hash_api
from springfield_chain.block.blocks import MAX_TX

HASH_PREFIX = '0000'

from springfield_chain.block.blocks import Block

def is_proven_hash(hash):
    return hash.startswith(HASH_PREFIX)

def check_block(block):
    if not block.is_valid():
        return False
    h = hash_api.hash_block(block)
    return is_proven_hash(h)

def mine_proof(block, proof=0, n=10000000):
    """ calculates a valid proof for a new block candidate """
    if not block.is_valid():
        raise ValueError('this block is not valid')
    for p in range(proof, proof + n):
        h = hash_api.hash_block_with_proof(block, p)
        if is_proven_hash(h):
            return p
        else:
            p += 1
    return None

def mine_block(last_block, tx_candidate_list):
    """ takes up to n tx from the candidate list """
    last_hash = hash_api.hash_block(last_block)
    print(str(last_block))
    new_block = Block(last_block.index + 1, last_hash)
    for tx in tx_candidate_list[:5]:
        new_block.add_transaction(tx)
    proof = mine_proof(new_block)
    new_block.set_proof(proof)
    return new_block

