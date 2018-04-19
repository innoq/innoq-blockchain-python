from springfield_chain.hashing import hash_api

def is_proven_hash(hash):
    return hash.startswith('0000')

def check_block(block):
    h = hash_api.hashBlock(block)
    return is_proven_hash(h)

def mine_block(block, proof=0, n=10000000):
    while (p in range(proof, proof + n)):
        h = hash_api.hashBlockWithProof(block, p)
        if is_proven_hash(h):
            block.set_proof(p)
            return block
        else:
            p += 1

def mine_block_parallel(block):
    mine_block(block)