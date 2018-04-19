from block.chain import BlockChain
import json

with open('block/genesis.json') as in_file:
    genesis = json.loads(in_file.read())

chain = BlockChain(genesis)

for block in chain:
    print(f'block: {block}')
