import json

from springfield_chain.mining import mining

with open('../block/genesis.json') as json_data:
    data = json.load(json_data)
    proof = mining.mine_block(data, 1900000, 100000)
    print("Mined proof: " + str(proof))
