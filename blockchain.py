import datetime
import hashlib
import json
from flask import Flask, jsonify

# Building a blockchain

class Blockchain:
    
    def __init__(self):
        #empty list that will contain blocks
        self.chain = []
        #genesis block - first block of blockchain
        #'0' in single quote as SHA-256 accepts only encoded strings
        self.create_block(proof = 1, previous_hash = '0')
        
    
    #this will create block once it is mined
    def create_block(self, proof, previous_hash):
        ''' Creating block with all the things required in block'''
        
        block = { 'index' : len(self.chain)+1 ,
                  'timestamp' : str(datetime.datetime.now()),
                  'proof' : proof,
                   'previous_hash' : previous_hash
                 }
        
        #adding block in the chain of blocks
        self.chain.append(block)
        return block
    
    
    def get_previous_block(self):
        '''Return the last block of the chain'''
        return self.chain[-1]
    
    
    def proof_of_work(self,previous_proof):
        '''check the proof of work, to add the block into the blockchain'''
        new_proof = 1
        check_proof = False
        while check_proof is False:
            #This is the complex operation equation that miners will solve
            #Equation should be encoded in strings as the requirement of SHA256 and return the hexadecimal form from SHA object
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            
            #if the hash_operation has starting 4 zeros then miner won
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1 #Go with the next value to try for the solving of equation
        return new_proof
    
    
    def hash(self,block):
        '''Returns the SHA256 HASH'''
        #json we have used as our block is in dictionary form
        encoded_block = json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    
    def is_chain_valid(self,chain):
        '''Checking whether the chain is valid or not'''
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            #if the previous hash value of block is not equal to the hash of previous block
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    
    
    
# Mining our Blockchain


## Create a web app
app = Flask(__name__)

## Create a blockchain
blockchain = Blockchain()

## Mining a new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    #return previous block
    previous_block = blockchain.get_previous_block()
    #returns previous proof of block
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    
    #get previous hash
    previous_hash = blockchain.hash(previous_block)
    
    #create block function invoked
    block = blockchain.create_block(proof, previous_hash)
    
    response = {'message' : 'Congratulations, you just mined a block!',
                'index' : block['index'],
                'timestamp' = block['timestamp'],
                'proof' : block['proof'],
                'previous_hash' : block['previous_hash']
                }
    return jsonify(response), 200 #for the HTTP status code
    
    
    
    
    
    
    
    