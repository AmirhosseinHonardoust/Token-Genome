// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ReflectionToken {
    string public name = "ReflectionToken";
    mapping(address => uint256) public balanceOf;
    uint256 public reflectionFee = 500;
    address public owner;

    modifier onlyOwner(){ require(msg.sender==owner, "not owner"); _; }

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function setReflectionFee(uint256 newFee) external onlyOwner {
        reflectionFee = newFee;
    }

    function transfer(address to, uint256 amount) external returns(bool){
        uint256 fee = (amount * reflectionFee) / 10000;
        uint256 receiveAmount = amount - fee;

        balanceOf[msg.sender] -= amount;
        balanceOf[to] += receiveAmount;
        balanceOf[address(this)] += fee;

        return true;
    }
}
