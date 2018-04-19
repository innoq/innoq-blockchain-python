
class BlockChain:
    """
    represents the whole chain
    needs at least a genesis block
    """

    def __init__(self, genesis):
        self.chain = [genesis,]

    def __len__(self):
        return len(self.chain)

    def __iter__(self):
        return self.chain.__iter__()

    def next(self):
        return self.chain.next()

    def append(self, new_block):
        # TODO check integrity here?
        self.chain.append(new_block)
