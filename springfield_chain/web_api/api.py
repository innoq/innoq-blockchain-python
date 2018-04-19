from flask import Flask

import time
from springfield_chain.web_api.node import Node
from springfield_chain.block.blocks import Block
from springfield_chain.hashing import hash_api
from springfield_chain.mining import mining

app = Flask(__name__)

node = Node('springfield_chain/block/genesis.json')

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + node.uuid + '", "currentBlockHeight": ' + str(len(node.chain)) +'}'


@app.route('/blocks')
def get_blocks():
        return '{"blocks":' + node.chain.toJSON() + '}'


@app.route('/mine')
def get_mine():
        time_start = time.clock()
        last_block = node.chain[-1]
        last_hash = hash_api.hash_block(last_block)
        print (str(last_block))
        new_block = Block(last_block['index'] + 1, last_hash)
        #proof = mining.mine_block(new_block)
        #new_block.set_proof(proof)
        node.chain.append(new_block)
        time_end = time.clock()
        return '{"message": "Mined a new block in ' + str(time_end-time_start) + 's", "block":' + new_block.toJSON() + '}'

# FIXME implement
@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"