// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RugTaxToken {
    mapping(address => uint256) public balanceOf;
    uint256 public tax;
    address public owner;

    modifier onlyOwner(){ require(msg.sender==owner, "not owner"); _; }

    constructor(){
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function setTax(uint256 newTax) external onlyOwner {
        tax = newTax; // can be 10000 = 100%%
    }

    function transfer(address to, uint256 amount) external returns(bool){
        uint256 t = (amount * tax) / 10000;
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += (amount - t);
        return true;
    }
}
