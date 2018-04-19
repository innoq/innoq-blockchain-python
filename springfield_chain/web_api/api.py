from flask import Flask
from springfield_chain.block import blocks
import uuid
from springfield_chain.block.chain import BlockChain
import json

app = Flask(__name__)

with open('springfield_chain/block/genesis.json') as in_file:
    genesis = json.loads(in_file.read())

chain = BlockChain(genesis)

UUID = str(uuid.uuid1())

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + UUID + '", "currentBlockHeight": ' + str(len(chain)) +'}'


@app.route('/blocks')
def get_blocks():
        return blocks.dummyBlocks()


@app.route('/mine')
def get_mine():
        return '"Hello, mine!'


@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"