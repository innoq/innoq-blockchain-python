from flask import Flask
from springfield_chain.block.chain import BlockChain
import uuid
import json

app = Flask(__name__)

chain = BlockChain()

UUID = str(uuid.uuid1())

@app.route('/')
def get_node_information():
        return '{"nodeId": "' + UUID + '", "currentBlockHeight": ' + str(len(chain)) +'}'


#FIXME returns wrong data structure
@app.route('/blocks')
def get_blocks():
        return json.dumps(chain.__dict__)

#FIXME implement
@app.route('/mine')
def get_mine():
        return "dummy miner"

# FIXME implement
@app.route("/nodes/register", methods=["POST"])
def register_node ():
        return "dummy registration"