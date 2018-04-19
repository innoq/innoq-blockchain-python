from flask import Flask

import json
from springfield_chain.web_api.node import Node

app = Flask(__name__)

node = Node('springfield_chain/block/genesis.json')

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + node.uuid + '", "currentBlockHeight": ' + str(len(node.chain)) +'}'


@app.route('/blocks')
def get_blocks():
        return '{"blocks":' + json.dumps(node.chain) + '}'

#FIXME implement
@app.route('/mine')
def get_mine():
        return "dummy miner"

# FIXME implement
@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"