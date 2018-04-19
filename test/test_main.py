import json

from springfield_chain.hashing import hash_api

from springfield_chain import __version__


def test_metadata():
    assert __version__ == '0.0.1'


def test_hash():
    with open('./springfield_chain/block/genesis.json') as json_data:
        data = json.load(json_data)
        assert hash_api.hashBlock(data) == '000000b642b67d8bea7cffed1ec990719a3f7837de5ef0f8ede36537e91cdc0e'


def test_hash_with_proof():
    with open('./springfield_chain/block/genesis.json') as json_data:
        data = json.load(json_data)
        assert hash_api.hashBlockWithProof(data, 123) == '60a943ad0e679aa56dd2359927ea655e09254df82a06e7b48c3eca1de5161de0'
