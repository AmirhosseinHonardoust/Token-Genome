// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Proxy {
    address public implementation;
    address public admin;

    constructor(address impl) {
        implementation = impl;
        admin = msg.sender;
    }

    function upgrade(address newImpl) external {
        require(msg.sender == admin, "not admin");
        implementation = newImpl;
    }

    fallback() external payable {
        address impl = implementation;
        assembly {
            calldatacopy(0, 0, calldatasize())
            let r := delegatecall(gas(), impl, 0, calldatasize(), 0, 0)
            returndatacopy(0, 0, returndatasize())
            switch r
            case 0 { revert(0, returndatasize()) }
            default { return(0, returndatasize()) }
        }
    }
}
