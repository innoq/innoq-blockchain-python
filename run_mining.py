from springfield_chain.mining.mining import mine_block
from springfield_chain.block.blocks import block_from_dict
import json
import sys

DEBUG = True
# expecting arguments proof(int), num_tries(int) and serialized json of block
if DEBUG:
    for arg in sys.argv:
        print(f'arg: {arg}')


proof = int(sys.argv[1])
num_tries = int(sys.argv[2])
block_string = ' '.join(sys.argv[3:])
print(f'block: {block_string}')
block = block_from_dict(json.loads(block_string))

res = mine_block(block, proof, num_tries)

if res is None:
    sys.exit(0)
else:
    print(res.proof)
    sys.exit(0)