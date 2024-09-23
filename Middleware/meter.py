import os
import colours
import blockchainConnector as bc

address = '0x5fbdb2315678afecb367f032d93f642f64180aa3'  #change every depoly
abi_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'abi.json')
if __name__ == '__main__':
    bc.loadTokenContract(address=address,abi_file=abi_file)
    colours.printGreen("contract name is %s"%bc.getFunctions())
    colours.printGreen("contract name is %s"%bc.getName())