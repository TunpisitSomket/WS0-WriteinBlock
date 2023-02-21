import json
import configparser
from web3 import Web3


class Blockchain:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        self.url = config['SETTINGS']['ganache_url']
        self.web3 = Web3(Web3.HTTPProvider(self.url))
        self.web3.eth.defaultAccount = self.web3.eth.accounts[0]
        self.abi = json.loads(config['ABI']['abi_json'])
        self.abi_address = config['ABI']['abi_address']
        self.contract = self.web3.eth.contract(address=self.abi_address, abi=self.abi)

    def set_name(self, name):
        tx_hash = self.contract.functions.setName(name).transact()
        transaction_receipt = self.web3.eth.waitForTransactionReceipt(tx_hash)
        return transaction_receipt['transactionHash'].hex()

    def hi(self):
        return self.contract.functions.hi().call()
