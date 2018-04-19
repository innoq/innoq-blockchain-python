from flask import Flask
app = Flask(__name__)

@app.route('/')
def get_node_information():
        return '{"nodeId": "Hello, World!"}'


@app.route('/blocks')
def get_blocks():
        return '"Hello, blocks!'

@app.route('/mine')
def get_mine():
        return '"Hello, mine!'