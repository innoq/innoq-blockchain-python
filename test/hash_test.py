import json

from springfield_chain.block.blocks import block_from_dict
from springfield_chain.hashing import hash_api

with open('springfield_chain/block/genesis.json') as json_data:
    data = json.load(json_data)
    block = block_from_dict(data)
    print(hash_api.hash_block_with_proof(block, 1917336))
