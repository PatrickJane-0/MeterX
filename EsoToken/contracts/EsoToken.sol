// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./MeterManagement.sol";
import "hardhat/console.sol";
// Bottom most child contract conforming to ERC20 token standard
contract EsoToken is MeterManagement {
    string constant kname = "Eso Token: 1 token = 1kWh";
    string constant ksymbol = "Eso";
    uint8 constant kdecimals = 6; // Defines number of decimal places for Krag Token 
    
    
    constructor()
        MeterManagement(kname,ksymbol,kdecimals)
    {
        console.log("EsoToken constructor msg.sender is  %s",msg.sender);
    }
}