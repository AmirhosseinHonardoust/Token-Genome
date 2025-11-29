// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AntiWhaleToken {
    string public name = "AntiWhale";
    mapping(address => uint256) public balanceOf;
    uint256 public maxTx = 10_000 ether;

    constructor() {
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function transfer(address to, uint256 amount) external returns(bool){
        require(amount <= maxTx, "maxTx exceeded");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
