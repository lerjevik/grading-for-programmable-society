const hre = require("hardhat");
const { OWNER_ADDRESS } = process.env;

async function main() {
  const initialOwner = OWNER_ADDRESS;

  const grading = await hre.ethers.deployContract("Grading", [initialOwner]);

  await grading.waitForDeployment();

  console.log("Contract deployed to address:", grading.target);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

