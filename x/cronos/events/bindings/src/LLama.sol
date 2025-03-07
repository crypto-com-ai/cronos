// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

interface ILLamaModule {
    function inference(string calldata prompt, int64 seed, int32 steps) external payable returns (string memory result);
}
