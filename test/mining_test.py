import json

from springfield_chain.mining import mining
from springfield_chain.block import blocks

with open('springfield_chain/block/genesis.json') as json_data:
    data = blocks.block_from_dict(json.load(json_data))
    proof = mining.mine_proof(data, 1900000, 100000)
    print("Mined proof: " + str(proof))
