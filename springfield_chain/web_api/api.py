import json

from flask import Flask, request, render_template

import time

from springfield_chain.block.transaction import Transaction
from springfield_chain.web_api.node import Node

from springfield_chain.mining import mining

app = Flask(__name__, template_folder='../app/templates')

node = Node('springfield_chain/block/genesis.json')


@app.route('/')
def get_node_information():
        return '{"nodeId": "' + node.uuid + '", "currentBlockHeight": ' + str(len(node.chain)) + ', "neighbours": ' + \
               json.dumps(node.neighbours) + '}'


@app.route('/blocks')
def get_blocks():
    return '{"blocks":' + node.chain.toJSON() + '}'


@app.route('/mine')
def get_mine():
    time_start = time.clock()
    last_block = node.chain[-1]
    new_block = mining.mine_block(last_block, node.candidate_txs)
    node.append_block(new_block)
    time_end = time.clock()
    return '{"message": "Mined a new block in ' + str(time_end - time_start) + 's", "block":' + new_block.toJSON() + '}'


@app.route('/transactions/<id>')
def get_transaction_by_id(id):
    tx = node.get_transaction_by_id(id)
    if tx is None:
        return '{"message": "No transaction found for %s"}' % id
    else:
        return json.dumps(tx)


@app.route('/transactions/new')
def get_transactions_new():
    return render_template("new_transaction.html")


@app.route('/transactions', methods=["POST"])
def post_transaction():
    if request.json is None:
        payload = request.form['payload']
    else:
        request_data = request.get_json()
        payload = request_data['payload']
    print(f'payload: {payload}')
    tx = Transaction(payload)
    node.append_transaction(tx)
    result = tx.copy()
    result['confirmed'] = False
    return json.dumps(result)


@app.route("/nodes/register", methods=["POST"])
def register_node ():
        request_data = request.get_json()
        host = request_data['host']
        print(f'host: {host}')
        neighbour = node.register_neighbour(host)
        return '{ "message": "New node added","node": ' + json.dumps(neighbour) + '}'
