# blockchain imports
from web3 import Web3, HTTPProvider
from eth_account import Account
from eth_account.signers.local import LocalAccount
# from web3.contract import ConciseContract

# other imports
import json
import colours
import sys,time
import os

web3Provider = 'http://127.0.0.1:8545/'

try:
    web3 = Web3(HTTPProvider(web3Provider))
    colours.printGreen("Connected to RPC blockchain endpoint on: "+web3Provider)
except:
    colours.printRed("Failed to connect to blockchain...closing")
    sys.exit()
_address = None
tokenContract = None

def loadTokenContract(address,abi_file):
    global tokenContract
    global _address
    _address = Web3.to_checksum_address(address)
    colours.printBlack("address is {}".format(_address))
    # if Web3.to_checksum_address(address) is not True:
    #     colours.printRed("Contract address toChecksumAddress failed...closing")
    #     sys.exit()
    if tokenContract == None:
        with open(abi_file) as f:
            abi = json.load(f)['abi']   #only need the abi part
        try:
            tokenContract = web3.eth.contract(abi=abi, address=_address)
            colours.printGreen("Token contract loaded!")
        except:
            colours.printRed("Token contract loading failed...closing")
            sys.exit()


def getTokenContractAddress():
    return _address


# def getNodeAddress(meter_addr):
#     return web3.eth.accounts[Web3.to_checksum_address(meter_addr)]

def createAccount():
    return web3.eth.account.create()

def getBalance(meter_addr):
    return tokenContract.functions.balanceOf(meter_addr).call()


def getTotalSupply():
    return tokenContract.functions.totalSupply().call() 


def getSymbol():
    return tokenContract.functions.symbol().call() 


def getName():
    return tokenContract.functions.name().call()    #or tokenContract.functions['name'].call()


def transfer(meter_addr,address_to, ammount):
    return tokenContract.transfer(address_to, ammount, transact={'from': web3.eth.accounts[meter_addr]})


def mintToken(account:LocalAccount,meter,value):
    transaction = {
        'nonce':web3.eth.get_transaction_count(account.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.meterMint(value,meter).build_transaction(transaction)
    signed_df_tx = account.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction)  


def burnToken(meter_addr,value):
    return tokenContract.functions.burn(value, transact={'from': web3.eth.accounts[meter_addr]}).call()

def enroleMeter(account:LocalAccount,meterAddress,ownerAddress):
    transaction = {
        'nonce':web3.eth.get_transaction_count(account.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.enroleMeter(meterAddress, ownerAddress).build_transaction(transaction)
    signed_df_tx = account.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction)  

def getmeterToOwner(meter_addr):
    return tokenContract.functions.meterToOwner(meter_addr).call()    #or tokenContract.functions['name'].call()


def mintTo(owner:LocalAccount,amount,recipient):
    transaction = {
        'nonce':web3.eth.get_transaction_count(owner.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.mintTo(amount, recipient).build_transaction(transaction)
    signed_df_tx = owner.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction) 

################ nft ####################################
def BidSubmit(account:LocalAccount,quantity,price):
    transaction = {
        'nonce':web3.eth.get_transaction_count(account.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.BidSubmit({'quantity':quantity, 'price':price}).build_transaction(transaction)
    signed_df_tx = account.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction) 

def offerSubmit(account:LocalAccount,quantity,price):
    transaction = {
        'nonce':web3.eth.get_transaction_count(account.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.offerSubmit({'quantity':quantity, 'price':price}).build_transaction(transaction)
    signed_df_tx = account.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction) 

def settleDataContract(owner:LocalAccount):
    transaction = {
        'nonce':web3.eth.get_transaction_count(owner.address),
        'gas': 2000000,
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
    }
    
    contruct_data = tokenContract.functions.settleDataContract().build_transaction(transaction)
    signed_df_tx = owner.sign_transaction(contruct_data)
    web3.eth.send_raw_transaction(signed_df_tx.raw_transaction) 

def getFunctions():
    return tokenContract.all_functions()
