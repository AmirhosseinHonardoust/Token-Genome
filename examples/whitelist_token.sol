// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract WhitelistToken {
    mapping(address => bool) public whitelist;
    mapping(address => uint256) public balanceOf;
    address public owner;

    modifier onlyOwner(){ require(msg.sender==owner, "not owner"); _; }

    constructor(){
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function setWhitelist(address user, bool allowed) external onlyOwner {
        whitelist[user] = allowed;
    }

    function transfer(address to, uint256 amount) external returns(bool){
        require(whitelist[msg.sender], "not whitelisted");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
