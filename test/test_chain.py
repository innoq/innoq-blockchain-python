from springfield_chain.block.chain import BlockChain
import json
import os

def test_chain_len():
    print(f'{os.getcwd()}')
    chain = create_simple_chain()
    assert len(chain) == 1

def test_chain_iterator():
    chain = create_simple_chain()
    for block in chain:
        assert json.dumps(block).startswith('{"index":')

def create_simple_chain():
    with open('springfield_chain/block/genesis.json') as in_file:
        genesis = json.loads(in_file.read())

    return BlockChain(genesis)