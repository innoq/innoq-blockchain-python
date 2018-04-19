from springfield_chain.hashing import hash_api

def isProvenHash(hash):
    return hash.startswith('0000')

def checkBlock(block):
    h = hash_api.hashBlock(block)
    return isProvenHash(h)

def mineBlock(block):
    p = 0
    while (True):
        h = hash_api.hashBlockWithProof(block, p)
        if isProvenHash(h):
            block.set_proof(p)
            return block
        else:
            p = p + 1