import hashlib
import datetime as date
from flask import Flask, jsonify, request
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, date.datetime.now(), 'Genesis Block', '0')

    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True
class Cryptocurrency:
    def __init__(self) -> None:
        self.blockchain = Blockchain()
     
    def mine_block(self):
        new_block = Block(len(self.blockchain.chain), date.datetime.now(), 'Maya_Coin', '')  
        self.blockchain.add_block(new_block)

    def get_full_chain(self):
        chain_data = []
        for block in self.blockchain.chain:
            block_data = {
                'index': block.index,
                'timestamp': str(block.timestamp),
                'data': block.data,
                'previous_hash': block.previous_hash,
                'hash': block.hash
            }

            chain_data.append(block_data)
            return jsonify({'chain': chain_data})

        app = Flask(__name__)
        Cryptocurrency = Cryptocurrency()

        @app.route('/mine_block', methods=['GET'])
        def mine_block():
            Cryptocurrency.mine_block()
            return 'Block mined successfully!'

        @app.route('/get_chain', methods=['GET'])
        def get_chain():
            return Cryptocurrency.get_full_chain()

        @app.route('/get_balance', methods=['POST'])
        def get_balance():
            address = request.get_json(['address'])
            return Cryptocurrency.get_balance(address)

        if __name__ == '__main__':
            app.run(port=5000)