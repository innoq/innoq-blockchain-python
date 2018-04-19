from flask import Flask
from springfield_chain.block.chain import BlockChain
import uuid

app = Flask(__name__)

chain = BlockChain()

UUID = str(uuid.uuid1())

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + UUID + '", "currentBlockHeight": ' + str(len(chain)) +'}'


@app.route('/blocks')
def get_blocks():
        return "blocks"


@app.route('/mine')
def get_mine():
        return "dummy miner"


@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"