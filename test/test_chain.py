from springfield_chain.block.chain import BlockChain
from springfield_chain.block.blocks import block_from_dict
import json
import os

def test_chain_len():
    print(f'{os.getcwd()}')
    chain = create_simple_chain()
    assert len(chain) == 1

def test_chain_iterator():
    chain = create_simple_chain()
    for block in chain:
        assert json.dumps(block.to_ordered_dict()).startswith('{"index":')

def create_simple_chain():
    with open('springfield_chain/block/genesis.json') as in_file:
        genesis = block_from_dict(json.loads(in_file.read()))

    return BlockChain(genesis)

