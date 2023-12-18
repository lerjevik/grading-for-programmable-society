// SPDX-License-Identifier: MIT
pragma solidity ^0.8.23;

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
* @title Grading for Course DD2485 
* @notice Students can be awarded with tokens representing assignments of the course and final course certificates
* @dev Implements the ERC1155 multi-token standard as well as Ownable to make functions only calleable by Owner
*/
contract Grading is ERC1155, Ownable {

    uint256 public constant Presentations = 0;
    uint256 public constant SmartContractProtocol = 1;
    uint256 public constant Demos = 2;
    uint256 public constant OpenSourceContributions = 3;
    uint256 public constant Feedback = 4;
    uint256 public constant Essays = 5;
    uint256 public constant Questions = 6;

    uint256 public constant GradeE = 7;
    uint256 public constant GradeD = 8;
    uint256 public constant GradeC = 9;
    uint256 public constant GradeB = 10;
    uint256 public constant GradeA = 11;

    constructor(address initialOwner) ERC1155("https://gateway.pinata.cloud/ipfs/QmZxkq1KwFvvfTFd1xnLXKbiThBiUvuMMJF7feJLfMU7Wk/{id}.json") Ownable(initialOwner) {}

    /**
    * @notice Allows teacher to publish images under new URI
    * @dev Only calleable by Owner
    * @param newuri The URI to be set
    */
    function setURI(string memory newuri) public onlyOwner {
        _setURI(newuri);
    }

    /**
    * @notice Allows teacher to burn tokens (e.g., when a mistake occurred in grading)
    * @dev Only calleable by Owner
    * @param account Address of account where tokens will be burned
    * @param id ID of token to be burned
    * @param amount Amount of tokens to be burned
    */
    function burn(address account, uint256 id, uint256 amount) public onlyOwner {
        _burn(account, id, amount);
    }

    /**
    * @notice Allows teacher to burn tokens of different IDs and quantities simultaneously for a student 
    * @dev Only calleable by Owner
    * @param account Address of account where tokens will be burned
    * @param ids Array with IDs of tokens to be burned
    * @param amounts Array with amount of tokens to be burned for each ID
    */
    function burnBatch(address account, uint256[] memory ids, uint256[] memory amounts) public onlyOwner {
        for (uint i=0; i<ids.length; i++){
            burn(account, ids[i], amounts[i]);
        }
    }

    /**
    * @notice Allows teacher to mint tokens for a student 
    * @dev Only calleable by Owner. Implements checkAmounts modifier
    * @param account Address of account where tokens will be minted
    * @param id ID of token to be minted
    * @param amount Amount of tokens to be minted
    */
    function mint(address account, uint256 id, uint256 amount) public onlyOwner checkAmounts(account, id, amount) {
        _mint(account, id, amount, "0x0");
    }

    /**
    * @notice Allows teacher to mint tokens of different IDs and quantities simultaneously for a student 
    * @dev Only calleable by Owner
    * @param account Address of account where tokens will be minted
    * @param ids Array with IDs of tokens to be minted
    * @param amounts Array with amount of tokens to be minted for each ID
    */
    function mintBatch(address account, uint256[] memory ids, uint256[] memory amounts) public onlyOwner {
        for (uint i=0; i<ids.length; i++){
            mint(account, ids[i], amounts[i]);
        }
    }

    /**
    * @notice Ensures that the maximum quantity of respective token per student is respected
    * @dev Modifier used in mint and indirectly in mintBatch using mintBatchHelper. Account can have at most one token of each kind
    * @param account Address of account to check balance of
    * @param id ID of token to check balance of
    * @param amount Maximum amount of tokens that can be added to students account
    */
    modifier checkAmounts(address account, uint256 id, uint256 amount){
            if(balanceOf(account, id) == 0){
                require(amount==1 || amount==0, "Student can't have more than 1 of this token");
            }
            else{
                require(amount==0, "Student can't have more than 1 of this token");
            }
    
        _;
    }

    /**
    * @notice Called by teacher to craft a course grade certificate for a student based on number of tokens
    * @dev Only calleable by Owner. Requires 3 mandatory tasks
    * @param account Address of account to allocate certificate to
    */
    function certificateAllocation(address account) public onlyOwner {
        uint256 sumMandatoryTasks = 0;
        for(uint256 i = 0; i <= 2; i++) 
            sumMandatoryTasks = sumMandatoryTasks + balanceOf(account,i); 
        
        uint256 sumOptionalTasks = 0;
        for(uint256 j = 3; j <= 6; j++) 
            sumOptionalTasks = sumOptionalTasks + balanceOf(account,j);
        
        require(sumMandatoryTasks == 3, "Student must have passed mandatory tasks");
        
        if(sumOptionalTasks == 0)
        {
            mint(account, 7, 1); // Mint 1 GradeE
        }
        else if(sumOptionalTasks == 1)
        {
            mint(account, 8, 1); // Mint 1 GradeD
        } 
        else if(sumOptionalTasks == 2)
        {
            mint(account, 9, 1); // Mint 1 GradeC
        } 
        else if(sumOptionalTasks == 3)
        {
            mint(account, 10, 1); // Mint 1 GradeB
        }
        else
        {
            mint(account, 11, 1); // Mint 1 GradeA
        } 
    }
}
