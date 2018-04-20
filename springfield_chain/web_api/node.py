import uuid
import json
from springfield_chain.block.chain import BlockChain
from springfield_chain.block.blocks import block_from_dict


class Node:

    def __init__(self, persistence_file=None):
        self.uuid = str(uuid.uuid1())
        with open(persistence_file) as in_file:
            genesis = block_from_dict(json.loads(in_file.read()))

        self.chain = BlockChain(genesis)
        self.transactions = []

    def append_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transaction_by_id(self, id, trans=None):
        for trx in self.transactions:
            if trx.id == id:
                print("woohooo")
                trans = trx
        # FIXME
        return '{ "id": "' + str(trans.id) + '","payload": "' + str(trans.payload) + ',"timestamp": ' \
               + str(trans.timestamp) + ',"confirmed": true}'
