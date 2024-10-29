# meterblock
**Blockchain facilitated energy exchange for open-grid applications**
us requirement:
Smart meters are the key devices in smart grid systems. They are used to measure the usage of electricity and communicate with the power plant for other functionalities such as calculating the bills,
 bidding the price, demanding the amount of the electricity ect. A severe concern of deploying such smart devices is that the information collected by the smart meters are sent to the power plant which 
 may glimpse user privacy from the received data, e.g., a user is probably at home in the hours that the usage of the electricity is at peak. Therefore, a trusted mediator is a straightforward solution 
 to handle the data processing, bill calculating, price bidding and electricity allocating. As blockchain is a trusted decentralised authority which provide security, it is a perfect mediator for the 
 above mentioned tasks. This project aims to 
(1) Design a blockchain based mediator for the smart grid system which provide better privacy for users 
(2) Formally verify the security and privacy of the design

# Sample Hardhat Project

This project demonstrates a basic Hardhat use case. It comes with a sample contract, a test for that contract, and a Hardhat Ignition module that deploys that contract.

Try running some of the following tasks:

```shell
npx hardhat help
npx hardhat test
REPORT_GAS=true npx hardhat test
npx hardhat node
npx hardhat ignition deploy ./ignition/modules/Lock.js
```
#run a local node:
npx hardhat node
#build
npx hardhat compile
#deploy:
npx hardhat ignition deploy ./ignition/modules/EsoToken.js --network localhost
#example
python3 tool.py


