// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract PausableToken {
    bool public tradingEnabled = false;
    address public owner;
    mapping(address => uint256) public balanceOf;

    modifier onlyOwner(){ require(msg.sender==owner, "not owner"); _; }

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = 1_000_000 ether;
    }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
    }

    function transfer(address to, uint256 amount) external returns(bool){
        require(tradingEnabled, "trading disabled");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        return true;
    }
}
