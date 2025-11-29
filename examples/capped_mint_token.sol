// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CappedMintToken {
    string public name = "CappedMint";
    uint256 public maxSupply = 1_000_000 ether;
    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;
    address public owner;

    modifier onlyOwner() { require(msg.sender == owner, "not owner"); _; }

    constructor() { owner = msg.sender; }

    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply + amount <= maxSupply, "cap exceeded");
        totalSupply += amount;
        balanceOf[to] += amount;
    }
}
