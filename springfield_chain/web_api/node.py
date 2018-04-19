import uuid
import json
from springfield_chain.block.chain import BlockChain

class Node:

    def __init__(self, persistence_file=None):
        self.uuid = str(uuid.uuid1())
        with open(persistence_file) as in_file:
            genesis = json.loads(in_file.read())

        self.chain = BlockChain(genesis)

