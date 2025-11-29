// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract UnlimitedMintToken {
    string public name = "UnlimitedMint";
    string public symbol = "UMT";
    mapping(address => uint256) public balanceOf;
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "not owner");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    function mint(address to, uint256 amount) external onlyOwner {
        balanceOf[to] += amount;
    }
}
