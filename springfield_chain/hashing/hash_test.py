import json

from springfield_chain.block.blocks import Block
from springfield_chain.hashing import hash_api

with open('../block/genesis.json') as json_data:
    data = json.load(json_data)
    block = Block(data["index"], data["previousBlockHash"], data["timestamp"])
    for tx in data["transactions"]:
        block.add_transaction(tx["id"], tx["timestamp"], tx["payload"])
    print(hash_api.hashBlockWithProof(block.to_ordered_dict(), 1917336))
