// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CooldownToken {
    mapping(address => uint256) public balanceOf;
    mapping(address => uint256) public lastTransfer;
    uint256 public cooldown = 30 seconds;

    constructor() {
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function transfer(address to, uint256 amount) external returns(bool){
        require(block.timestamp >= lastTransfer[msg.sender] + cooldown, "cooldown active");
        lastTransfer[msg.sender] = block.timestamp;
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
