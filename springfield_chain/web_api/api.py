from flask import Flask
from springfield_chain.block import blocks
import uuid

app = Flask(__name__)

UUID = str(uuid.uuid1())

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + UUID + '", "currentBlockHeight": 0}'


@app.route('/blocks')
def get_blocks():
        return blocks.dummyBlocks()


@app.route('/mine')
def get_mine():
        return '"Hello, mine!'


@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"