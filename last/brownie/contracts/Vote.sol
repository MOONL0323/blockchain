// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Vote {
    mapping (address => bool) public votes;

    function vote() public {
        require(!votes[msg.sender], "You have already voted.");
        votes[msg.sender] = true;
    }
}