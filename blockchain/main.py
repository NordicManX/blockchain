import hashlib
import datetime as date

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

my_blockchain = Blockchain()

purchase1 = {
    'item': 'Ford Mustang',
    'value': 100.000,
    'buyer': 'nelson@gmail.com',
    'seller': '@cazuza'
}

purchase2 = {
    'item': 'Ferrari',
    'value': 600.000,
    'buyer': 'vendas@ouel.com',
    'seller': '@camarão'
}

purchase3 = {
    'item': 'camaro',
    'value': 80.000,
    'buyer': 'vendas@ouel.com',
    'seller': '@camarão'
}

doc = {
    'item': 'DOC. test document',
    'valuePaidToTheResource': 100,
    'buyer': 'pati@liça.com',
    'seller': '@cartorio'
}

my_blockchain.add_block(Block(1, date.datetime.now(), purchase1, my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(2, date.datetime.now(), purchase2, my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(3, date.datetime.now(), purchase3, my_blockchain.chain[-1].hash))
my_blockchain.add_block(Block(4, date.datetime.now(), doc, my_blockchain.chain[-1].hash))


print(f'Blockchain is valid? {my_blockchain.is_valid()}')


def print_blockchain(chain):

    print(30*'-----')

    for block in chain:
        
        print(f'Block: {block.index}')
        print(f'Timestamp: {block.timestamp}')
        print(f'Dados Salvos: {block.data}')
        print(f'Hash: {block.hash}')
        print(f'Previous Hash: {block.previous_hash}')
        print(30*'-----')

print(print_blockchain(my_blockchain.chain))