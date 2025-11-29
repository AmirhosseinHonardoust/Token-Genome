// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RebaseToken {
    string public name = "RebaseToken";
    uint256 public totalSupply = 1_000_000 ether;
    mapping(address => uint256) public balanceOf;
    address public owner;

    modifier onlyOwner(){ require(msg.sender == owner, "not owner"); _; }

    constructor() {
        owner = msg.sender;
        balanceOf[msg.sender] = totalSupply;
    }

    function rebase(int256 supplyDelta) external onlyOwner {
        if (supplyDelta > 0) {
            uint256 amount = uint256(supplyDelta);
            totalSupply += amount;
            balanceOf[owner] += amount;
        } else {
            uint256 remove = uint256(-supplyDelta);
            totalSupply -= remove;
            balanceOf[owner] -= remove;
        }
    }
}
