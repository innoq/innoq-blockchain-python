import json

from springfield_chain.block.blocks import Block
from springfield_chain.hashing import hash_api

with open('../block/genesis.json') as json_data:
    data = json.load(json_data)
    print(hash_api.hashBlockWithProof(data, 1917336))
