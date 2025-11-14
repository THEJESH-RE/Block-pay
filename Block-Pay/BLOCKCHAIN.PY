import json
import time
from hashlib import sha256

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp or time.time()
        self.transactions = transactions
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "nonce": self.nonce
        }, sort_keys=True)
        return sha256(content.encode()).hexdigest()

class PermissionedBlockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.flagged_transactions = []
        self.authorities = set()
        self.create_genesis_block()

    def create_genesis_block(self):
        self.chain.append(Block(0, "0", []))

    def add_authority(self, authority_name):
        self.authorities.add(authority_name)

    def add_transaction(self, transaction):
        if self.is_fraudulent(transaction):
            transaction['status'] = 'Flagged'
            self.flagged_transactions.append(transaction)
        else:
            transaction['status'] = 'Valid'
            self.pending_transactions.append(transaction)

    def is_fraudulent(self, transaction):
        suspicious_keywords = ["fraud", "hack", "scam", "illegal"]
        if any(word in transaction['description'].lower() for word in suspicious_keywords):
            return True
        return transaction['amount'] > 10000

    def mine_block(self, validator):
        if validator not in self.authorities:
            return "Unauthorized validator!"

        new_block = Block(len(self.chain), self.chain[-1].hash, self.pending_transactions)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block.hash
