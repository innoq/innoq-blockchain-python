import json

from springfield_chain.hashing.hash_api import hash_block
from springfield_chain.mining.mining import check_block


class BlockChain(list):
    """
    represents the whole chain
    needs at least a genesis block
    """

    def __init__(self, genesis):
        super().__init__([genesis])
        self.last_hash = hash_block(genesis)

    def append(self, new_block):
        """
        Checks a candidate block and (upon successful checks) adds it to the chain
        :param new_block:
        :return: true if successful, false if block was rejected
        """
        if self.check_new_block_validity(new_block):
            super().append(new_block)
            self.last_hash = hash_block(new_block) # TODO avoid computing hash twice
            return True
        else:
            return False

    def check_new_block_validity(self, new_block):
        if self.last_hash != new_block.previousBlockHash:
            print("last hash mismatch")
            return False
        elif check_block(new_block):
            print("invalid new block")
            return False
        else:
            return True

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
