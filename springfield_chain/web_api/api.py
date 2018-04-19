from flask import Flask
from springfield_chain.block import blocks

app = Flask(__name__)

@app.route('/')
def get_node_information():
        return '{"nodeId": "Hello, World!"}'


@app.route('/blocks')
def get_blocks():
        return blocks.dummyBlocks()

@app.route('/mine')
def get_mine():
        return '"Hello, mine!'