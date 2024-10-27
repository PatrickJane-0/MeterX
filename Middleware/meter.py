import sys,os,json,time
import colours
from eth_account import Account
from eth_account.signers.local import LocalAccount
import blockchainConnector as bc
from controllerSimulation import controllerSimulation
from controllerInterface import controllerBasic

Contract_address = '0x5fbdb2315678afecb367f032d93f642f64180aa3'  #change every depoly
abi_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),'abi.json')

# returns current mWh power consumption/production
def calcEnergy(power, time):
    return ((power * time) / 3600) * 1000

class Meter(controllerSimulation):
    def __init__(self,merter_file):
        try:
            with open(merter_file) as f:
                meter_conf = json.load(f)
                self._name=meter_conf["name"]
                self._address = meter_conf["address"]
                self._pri_key=meter_conf["pri_key"]
                self._owner=meter_conf["owner_key"]
                self._account:LocalAccount = Account.from_key(self._owner)
                super().__init__(meter_conf["simulation"])
        except:
            colours.printRed("merter_file:%s loading failed...closing"%merter_file)
            sys.exit()

def create_meter():
    account=bc.createAccount()
    colours.printPurple("create new account,address:%s,private key :%s"%(account.address,account.key.hex()))


if __name__ == '__main__':
    abi_file = r"/home/chao/work/MeterX/EsoToken/artifacts/contracts/EsoToken.sol/EsoToken.json"
    bc.loadTokenContract(address=Contract_address,abi_file=abi_file)
    # account=create_meter()
    # sys.exit()
    colours.printLightPurple("contract name is %s"%bc.getFunctions())
    colours.printGreen("contract name is %s"%bc.getName())
    colours.printGreen("contract symbol is %s"%bc.getSymbol())
    meter=Meter("/home/chao/work/MeterX/Middleware/meter2.json")
    meter.powerOn()
    colours.printGreen("meter balance is %d"%bc.getBalance(meter._address))
    colours.printGreen("meter owner is %s"%bc.getmeterToOwner(meter._address))
    # colours.printGreen(f"meter getNodeAddress :{bc.getNodeAddress(meter._address)}")
    colours.printGreen(f"meter isConsuming :{meter.isConsuming()}")
    
    polingDelay = 1
    StartingBalance = 100
    startTime = 0
    energyConsumed = 0
    showDisplay = True
    # Infinite loop to poll status of the meter
    while True:
        endTime = time.time()  # end time of previous consumption period
        #We dont decrement on the initial sample as this has not end time so the value would be incorrect for
        #sample duration
        if startTime != 0:
            elapsedTime = endTime - startTime
            powerValue = meter.queryPower()
            if powerValue<50:
                powerValue=0
            
            isConsuming = meter.isConsuming()

            energyValue = int(calcEnergy(powerValue, elapsedTime))

            balance = bc.getBalance(meter._address)
            colours.printLightGray(f"balance :{balance},powerValue:{powerValue},elapsedTime:{elapsedTime}")
            colours.printLightGray(f"current:{meter.queryCurrent()},voltage:{meter.queryVoltage()},Power:{powerValue},energyValue:{energyValue}")
            if (isConsuming):
                # if the wallet ballance would be set to <0, make the token balance zero else decrement tokens
                
                if (balance- energyConsumed <= 0):
                    if balance > 0:
                        bc.burnToken(meter._account,balance)
                else:
                    bc.burnToken(meter._account,int(energyValue))
                # dl.createEntry(int(powerValue),bc.getBalance())
            else: #if the meter is not consuming, it is producing so mint
                bc.mintToken(meter._account,meter._address,int(energyValue))
                colours.printLightGray("mintToken by account :%s to address:%s ,value :%d"%(meter._account._address,meter._address,int(energyValue)))
            #     dl.createEntry(-int(powerValue),bc.getBalance())
            # if showDisplay:
            #     display.addRow([powerValue,round(elapsedTime,5),round(energyValue,5),bc.getBalance(),isConsuming])
            #     display.displayTable()
        startTime = time.time()
        # toggle light state based on ballance
        if bc.getBalance(meter._address) > 0 or meter.isConsuming()==False:
            meter.powerOn()
            
        else:
            meter.powerOff()
        time.sleep(polingDelay)