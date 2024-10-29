#install openzeppelin
npm install @openzeppelin/contracts
npx hardhat init    #create empty project
npx hardhat compile
#run a local node:
npx hardhat node
#build
npx hardhat compile
#deploy:
npx hardhat ignition deploy ./ignition/modules/EsoToken.js --network localhost