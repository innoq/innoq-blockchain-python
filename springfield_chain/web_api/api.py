import json

from flask import Flask, request

import time

from springfield_chain.block.transaction import Transaction
from springfield_chain.web_api.node import Node

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
        new_block = mining.mine_block(last_block)
        node.chain.append(new_block)
        time_end = time.clock()
        return '{"message": "Mined a new block in ' + str(time_end-time_start) + 's", "block":' + new_block.toJSON() + '}'


@app.route('/transactions/<id>')
def get_transaction_by_id(id):
        trx = node.get_transaction_by_id(id)
        if trx is None:
                return '{"message": "No transaction found for \'' + id + '\'"}'
        else:
                return trx.to_json()


@app.route('/transactions', methods=["POST"])
def post_transaction():
        request_data = request.get_json()
        payload = request_data['payload']
        transaction = Transaction(json.dumps(payload, separators=(",", ":")))
        node.append_transaction(transaction)
        return '{"message": "Received new transaction ' + str(transaction.id) + ' with payload ' + transaction.payload + \
               ' at ' + str(transaction.timestamp) + '"}'

# FIXME implement
@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"