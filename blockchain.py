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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    