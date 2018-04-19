import json

class BlockChain(list):
    """
    represents the whole chain
    needs at least a genesis block
    """

    def __init__(self, genesis):
        super().__init__([genesis])

    def append(self, new_block):
        # TODO check integrity here?
        super().append(new_block)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)