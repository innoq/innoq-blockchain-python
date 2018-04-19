from flask import Flask

import json
from springfield_chain.web_api.node import Node
from springfield_chain.block.blocks import Block
from springfield_chain.hashing import hash_api


app = Flask(__name__)

node = Node('springfield_chain/block/genesis.json')

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + node.uuid + '", "currentBlockHeight": ' + str(len(node.chain)) +'}'


@app.route('/blocks')
def get_blocks():
        return '{"blocks":' + json.dumps(node.chain) + '}'


@app.route('/mine')
def get_mine():
        last_block = node.chain[-1]
        last_hash = hash_api.hashBlock(last_block)
        print (str(last_block))
        new_block = Block(last_block['index'] + 1, last_hash)
        # FIXME generate and add proof
        node.chain.append(new_block)
        return '{"message": "Mined a new block in xx.xxx s", "block":' + new_block.toJSON() + '}'

# FIXME implement
@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"