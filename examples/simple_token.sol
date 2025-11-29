// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleToken {
    string public name = "Simple";
    uint public totalSupply = 1000;
    mapping(address=>uint) public balanceOf;
    constructor(){ balanceOf[msg.sender]=totalSupply; }
    function transfer(address to,uint a) external returns(bool){
        balanceOf[msg.sender]-=a;
        balanceOf[to]+=a;
        return true;
    }
}
