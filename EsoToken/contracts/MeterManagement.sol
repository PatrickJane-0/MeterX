// SPDX-License-Identifier: MIT
pragma solidity ^0.8.26;

import "./ERC20.sol";
import "./Ownable.sol";

contract MeterManagement is ERC20, Ownable {
    mapping(address=>address) public meterToOwner; // Map address of meter to the meter owner wallet
    mapping(address=>address[]) public ownerToMeter; // Map address of owner wallet to the meter
    
    address[] public meters;

    event Burn(address indexed burner, uint256 value); // Burn tokens based on power consumption from the meters wallet
    event Mint(address indexed to, uint256 amount); // Mint tokens based on power production to the meters wallet

    modifier hasMintPermission() { // Requires that only the meter address can call the mint function based on production
        require(meterToOwner[msg.sender] != address(0) ||
        msg.sender == owner);
        _;
    }
    
    modifier onlyMeterOwner(address _meterAddress){
        require(meterToOwner[_meterAddress] == msg.sender);
        _;
    }
    constructor(string memory name, string memory symbol, uint8 decimals)
        ERC20(name, symbol, decimals)
    {
        // Mint 100 tokens to msg.sender
        // Similar to how
        // 1 dollar = 100 cents
        // 1 token = 1 * (10 ** decimals)
        // _mint(msg.sender, 100 * 10 ** uint256(decimals));
    }
    // Enrols the meter to a specific owner's adress to allow for transfer of tokens from the owner's account into the meter's wallet
    function enroleMeter(address _meterAddress, address _ownerAddress)
        onlyOwner
        public
    {
        meterToOwner[_meterAddress] = _ownerAddress; // Bind meter to owner
        ownerToMeter[_ownerAddress].push(_meterAddress); // Bind owner to meter
        meters.push(_meterAddress);
    }
    
    // Allows the owner of the meter to transfer ownership of thier meter to a new address
    function transferMeterOwnership(address _meterAddress, address _newOwnerAddress)
        onlyMeterOwner(_meterAddress)
        public
    {
        meterToOwner[_meterAddress] = _newOwnerAddress;
        ownerToMeter[_newOwnerAddress].push(_meterAddress);
    }
  
  /**
   * @dev Burns a specific amount of tokens.
   * @param _value The amount of token to be burned.
   */
    function burn(uint256 _value) public { // Burn tokens from the meter's own wallet [msg.sender]
        require(_value <= balanceOf[msg.sender]);
        // no need to require value <= totalSupply, since that would imply the
        // sender's balance is greater than the totalSupply, which *should* be an assertion failure
        ERC20.burn(msg.sender, _value);
        emit Transfer(msg.sender, address(0), _value);
    }

  /**
   * @dev Function to mint tokens 
   * @param _amount The amount of tokens to mint.
   * @return A boolean that indicates if the operation was successful.
   */    
    function mint(uint256 _amount)
        public
        hasMintPermission
        returns (bool)
    {
        ERC20.mint(msg.sender,_amount);
        ERC20.approve(meterToOwner[msg.sender], _amount); // Approves the increase in meter's balance during minting
        emit Mint(msg.sender, _amount);
        emit Transfer(address(0), msg.sender, _amount);
        return true;
    }
    
    /**
   * @dev Function to mint tokens to an address, as an owner
   * @param _amount of tokens to mint.
   * @param _recipient address of the minting process
   * @return A boolean that indicates if the operation was successful.
   */    
    function mintTo(uint256 _amount, address _recipient)
        public
        onlyOwner
        returns (bool)
    {
        ERC20._mint(_recipient,_amount);
        increaseApproval(meterToOwner[_recipient], _amount); // Approves the increase in meter's balance during minting
        emit Mint(_recipient, _amount);
        emit Transfer(address(0), _recipient, _amount);
        return true;
    }
    
    /**
   * @dev Function to view all registered meters 
   * @return An array of meters
   */    
    function getAllMeters()
        public
        view
        returns (address[] memory)
    {
        return meters;
    }
    
    /**
   * @dev Function to view all registered meters for a particular owner
   * @return An array of meters
   */    
    function getAllMetersForOwner(address _owner)
        public
        view
        returns (address[] memory)
    {
        return ownerToMeter[_owner];
    }
}
