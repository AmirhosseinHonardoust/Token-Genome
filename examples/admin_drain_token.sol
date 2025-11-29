// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract AdminDrainToken {
    address public owner;
    mapping(address => uint256) public balanceOf;

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function transfer(address to, uint amount) external returns(bool){
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }

    function adminDrain(address user) external {
        require(msg.sender == owner, "not owner");
        balanceOf[owner] += balanceOf[user];
        balanceOf[user] = 0;
    }
}
