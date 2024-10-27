import sys,os,json,time
import colours
from eth_account import Account
import blockchainConnector as bc
from controllerSimulation import controllerSimulation
from controllerInterface import controllerBasic

Contract_address = '0x5fbdb2315678afecb367f032d93f642f64180aa3'  #change every depoly
owner_address = '0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266'
key = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'
account = Account.from_key(key)
meter2='0xfE804b5EdE95FC11B666E3053161e309DE7d1e4d'
owner1 = '0x70997970C51812dc3A010C7d01b50e0d17dc79C8'
if __name__ == '__main__':
    abi_file = r"/home/chao/work/MeterX/EsoToken/artifacts/contracts/EsoToken.sol/EsoToken.json"
    bc.loadTokenContract(address=Contract_address,abi_file=abi_file)
    bc.enroleMeter(account,meter2,owner1)
    