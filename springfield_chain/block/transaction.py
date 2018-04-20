import time
import uuid
import collections

class Transaction(collections.OrderedDict):

    def __init__(self, payload):
        super.__init__([('id', str(uuid.uuid1())), ('timestamp', int(time.time())), ('payload', payload)])
