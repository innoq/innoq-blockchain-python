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
        self.candidate_txs = []
        self.confirmed_txs = []

    def append_transaction(self, tx, confirmed=False):
        if not confirmed:
            self.candidate_txs.append(tx)
        else:
            self.confirmed_txs.append(tx)

    def confirm_transaction(self, tx_id):
        """ removes a tx with given id from the candidate list and places it into confirmed tx list """
        for i in range(len(self.candidate_txs)):
            tx = self.candidate_txs[i]
            if tx['id'] == tx_id:
                self.candidate_txs.pop(i)
                self.confirmed_txs.append(tx)
                return tx_id
        return None

    def get_transaction_by_id(self, id):
        trans = None
        for trx in self.candidate_txs:
            if trx['id'] == id:
                print("woohooo")
                trans = trx.copy()
        trans['confirmed'] = True
        return json.dumps(trans)
