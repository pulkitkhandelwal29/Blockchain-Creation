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
        
    