// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "hardhat/console.sol";
// 定义的新类型包含两个属性。
// 在合约外部声明结构体可以使其被多个合约共享。 在这里，这并不是真正需要的。
struct Description {
    uint start_time;
    uint end_time;
    uint left;  // left electricity
    uint max;
}

struct Ech {
    address issuer;
    bool is_selling;
    address to;
    uint32 price;
    Description info;
}

contract EsoNft is ERC721, ERC721Burnable, Ownable {
    uint256 private _nextTokenId;
    mapping(address=>uint256 []) public ownerToToken; // Map address of owner wallet to the tokenId
    Ech[] public properties;


    constructor(address initialOwner)
        ERC721("EsoNft", "MTK")
        Ownable(initialOwner)
    {
        console.log("EsoNft constructor owner is  %s",msg.sender);
        // properties = new Ech[](0);
    }

    function safeMint(address to,Description memory info) public returns(uint256){
        uint256 tokenId = _nextTokenId++;
        properties.push(Ech(to,false,address(0),0,info));
        _safeMint(to, tokenId);
        return tokenId;
    }

    // The following functions are overrides required by Solidity.

    function _update(address to, uint256 tokenId, address auth)
        internal
        override(ERC721)
        returns (address)
    {
        address from =  super._update(to, tokenId, auth);
        if (to != address(0)) {
            ownerToToken[to].push(tokenId);
        }
        if (from != address(0)) {
            delete ownerToToken[from];
        }
        return from;
    }

    function isSupply() public view returns(bool){
        // for()
    }

    function get_properties_len() external view returns(uint256){
        return properties.length;
    }

    function get_Ech(uint256 tokenId) external view returns(Ech memory){
        require(tokenId<properties.length,"tokenId not exist in properties");
        return properties[tokenId];
    }

    function update_Ech(uint256 tokenId,Ech memory propertie) external  {
        require(tokenId<properties.length,"tokenId not exist in properties");
        properties[tokenId] = propertie;
    }

    function sellEch(uint256 tokenId,uint32 price,address to) public
    {
        require(tokenId<properties.length,"tokenId not exist in properties");
        Ech storage target=properties[tokenId];
        target.is_selling = true;
        target.price = price;
        target.to = to;
        ERC721.approve(target.to,tokenId);
    }

    function buyEch(address buyer,uint256 tokenId) public
    {
        require(tokenId<properties.length,"tokenId not exist in properties");
        Ech storage target=properties[tokenId];
        require(target.to == buyer || target.to == address(0)," not target buyer ");
        target.is_selling=false;
        ERC721.transferFrom(ERC721.ownerOf(tokenId),buyer,tokenId);
    }
}