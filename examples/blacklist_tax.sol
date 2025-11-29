// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract BlacklistTax {
    address public owner;
    mapping(address=>bool) public blacklist;
    mapping(address=>uint) public balanceOf;
    uint public tax = 2000;

    modifier onlyOwner(){require(msg.sender==owner);_;}

    constructor(){
        owner=msg.sender;
        balanceOf[msg.sender]=1000;
    }

    function setBlacklist(address u,bool b) external onlyOwner {
        blacklist[u]=b;
    }

    function setTax(uint t) external onlyOwner {
        tax=t;
    }

    function transfer(address to,uint a) external returns(bool){
        require(!blacklist[msg.sender]);
        uint t=(a*tax)/10000;
        balanceOf[msg.sender]-=a;
        balanceOf[to]+=a-t;
        return true;
    }
}
