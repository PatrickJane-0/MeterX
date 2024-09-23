# blockchain imports
from web3 import Web3, HTTPProvider
# from web3.contract import ConciseContract

# other imports
import json
import colours
import sys
import os


# try:
#     meterID = int(os.environ['METERID'])
#     colours.printGreen("Enviroment Variable included! Using MeterID: " + str(meterID))

# except:
#     colours.printRed("Could not find meterID...please set the enviroment var")
#     sys.exit()


# web3Provider = 'http://localhost:8545'
# web3Provider = 'http://142.93.131.22:8545'
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


# def getNodeAddress():
#     return web3.eth.accounts[meterID]


def getBalance():
    return tokenContract.balanceOf(web3.eth.accounts[meterID])


def getTotalSupply():
    return tokenContract.totalSupply()


def getSymbol():
    return tokenContract.symbol()


def getName():
    return tokenContract.functions.name().call()    #or tokenContract.functions['name'].call()


def transfer(address_to, ammount):
    return tokenContract.transfer(address_to, ammount, transact={'from': web3.eth.accounts[meterID]})


def mintToken(value):
    return tokenContract.mint(value, transact={'from': web3.eth.accounts[meterID]})


def burnToken(value):
    return tokenContract.burn(value, transact={'from': web3.eth.accounts[meterID]})


def getFunctions():
    return tokenContract.all_functions()