// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ManualPriceOracle {
    address public owner;
    int public price;

    modifier onlyOwner(){require(msg.sender==owner);_;}

    constructor(){
        owner=msg.sender;
        price=100;
    }

    function setPrice(int p) external onlyOwner { price=p; }
    function getPrice() external view returns(int){ return price; }
}
