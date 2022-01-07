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