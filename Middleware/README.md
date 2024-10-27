This directory stores all the required files to link the blockchain, meter and hardware control (voltage/current sensor & load controller). The so called "Middleware"
# run
python3 tool.py

#create new private key
python -c "from web3 import Web3; w3 = Web3(); acc = w3.eth.account.create(); print(f'private key={w3.to_hex(acc.key)}, account={acc.address}')"