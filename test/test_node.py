import uuid

from springfield_chain.block.transaction import Transaction
from springfield_chain.web_api.node import Node


def test_get_transaction_by_id():
    node = Node('springfield_chain/block/genesis.json')
    payload = 'blablabla'
    transaction = Transaction(payload)
    node.append_transaction(transaction)
    assert node.get_transaction_by_id(transaction['id']) is not None


def test_get_transaction_by_id_is_None():
    node = Node('springfield_chain/block/genesis.json')
    assert node.get_transaction_by_id(str(uuid.uuid1())) is None
