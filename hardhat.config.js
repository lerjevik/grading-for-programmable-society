require("dotenv").config();
require("@nomicfoundation/hardhat-toolbox");
require("@nomicfoundation/hardhat-ethers");
const { CHAINSTACK_NODE, OWNER_PRIVATE_KEY } = process.env;

module.exports = {
  solidity: "0.8.23",
  defaultNetwork: "sepolia",
  networks: {
    hardhat: {},
    sepolia: {
      url: CHAINSTACK_NODE,
      accounts: [`0x${OWNER_PRIVATE_KEY}`],
    },
  },  
};