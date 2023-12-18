
const { expect } = require("chai");
const { loadFixture } = require("@nomicfoundation/hardhat-network-helpers");

describe("Grading Contract", function () {
    let contract;
    async function deploymentFunction(){
        const [owner, student, student2] = await ethers.getSigners();
        const TestContract = await ethers.getContractFactory("Grading");
        contract = await TestContract.deploy(owner.address);
        return {contract, owner, student, student2}
    };

    it("setURI: Transaction should be rejected if called by another student, but pass if called by owner", async function () {
        const { contract, owner, student } = await loadFixture(deploymentFunction);

        // Student tries to change URI
        await expect(contract.connect(student).setURI("https://dd2485-test.com/{id}.json")).to.be.rejected

        // Owner tries to change URI
        await contract.connect(owner).setURI("https://dd2485-test.com/{id}.json");
        expect(await contract.uri(0)).to.equal("https://dd2485-test.com/{id}.json");
    });

    it("burn: Transaction should be rejected if called by another student, but pass if called by owner", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Allocation of 1 "Presentations"-token to student
        await contract.connect(owner).mint(student, 0, 1);

        // Student2 tries to burn this token
        await expect(contract.connect(student2).burn(student, 0, 1)).to.be.rejected

        // Owner tries to burn this token
        await contract.connect(owner).burn(student, 0, 1);
        expect(await contract.balanceOf(student, 0)).to.equal(0);
    });

    it("mint: Transaction should be rejected if called by another student, but pass if called by owner", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Student2 tries to mint "GradeE"-certificate to student
        await expect(contract.connect(student2).mint(student, 7, 1)).to.be.rejected

        // Teacher tries to mint "GradeE"-certificate to student
        await contract.connect(owner).mint(student, 7, 1);
        expect(await contract.balanceOf(student, 7)).to.equal(1);
    });

    it("mint: Transaction should be rejected if students recieves more tokens than possible for the Token ID, else pass", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Allocation of 1 "GradeA"-token to student
        await contract.connect(owner).mint(student, 11, 1);

        // Teacher tries to mint another "GradeA"-certificate to student who already has one
        await expect(contract.connect(owner).mint(student, 11, 1)).to.be.rejected.revertedWith(
            "Student can't have more than 1 of this token"
          );

        // Teacher tries to mint multiple "GradeE"-certificates to student2
        await expect(contract.connect(owner).mint(student2, 7, 2)).to.be.rejected.revertedWith(
            "Student can't have more than 1 of this token"
          );

        // Teacher tries to mint one "GradeC"-certificate to student 
        await contract.connect(owner).mint(student, 9, 1);
        expect(await contract.balanceOf(student, 9)).to.equal(1);
    }); 

    it("mintBatch: Transaction should be rejected if called by another student, but pass if called by owner", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Student tries to mint 1 "Demos"-token and 1 "Feedback"-token to student2
        await expect(contract.connect(student).mintBatch(student2, [2,4], [1,1])).to.be.rejected

        // Teacher tries to mint 1 "Demos"-token and 1 "Feedback"-token to student
        await contract.connect(owner).mintBatch(student, [2,4], [1,1]);
        expect(await contract.balanceOf(student, 2)).to.equal(1);
        expect(await contract.balanceOf(student, 4)).to.equal(1);
    });

    it("mintBatch: Transaction should be rejected if students recieves more tokens than possible for respective Token ID, else pass", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Allocation of 1 "SmartContractProtocol"-token to student
        await contract.connect(owner).mint(student, 1, 1);

        // Teacher tries to give student another "SmartContractProtocol"-token as well as 1 "Essays"-token
        await expect(contract.connect(owner).mintBatch(student, [1,5], [1,1])).to.be.rejected.revertedWith(
            "Student can't have more than 1 of this token"
          );

        // Teacher tries to give student 0 "SmartContractProtocol"-token as well as 1 "Essays"-token
        await contract.connect(owner).mintBatch(student, [1,5], [0,1]);
        expect(await contract.balanceOf(student, 1)).to.equal(1);
        expect(await contract.balanceOf(student, 5)).to.equal(1);

        // Teacher tries to give student2 0 "SmartContractProtocol"-token as well as 1 "Essays"-token
        await contract.connect(owner).mintBatch(student2, [1,5], [0,1]);
        expect(await contract.balanceOf(student2, 1)).to.equal(0);
        expect(await contract.balanceOf(student2, 5)).to.equal(1);

        // Teacher tries to give student2 1 "SmartContractProtocol"-token as well as 1 "OpenSourceContributions"-token
        await contract.connect(owner).mintBatch(student2, [1,3], [1,1]);
        expect(await contract.balanceOf(student2, 1)).to.equal(1);
        expect(await contract.balanceOf(student2, 3)).to.equal(1);
        
        // Teacher tries to give student 2 "Presentations"-token as well as 1 "OpenSourceContributions"-token
        await expect(contract.connect(owner).mintBatch(student, [0,3], [2,1])).to.be.rejected.revertedWith(
            "Student can't have more than 1 of this token"
          );

        // Teacher tries to give student 1 "SmartContractProtocol"-token 7 times
        await expect(contract.connect(owner).mintBatch(student, [1,1,1,1,1,1,1], [1,1,1,1,1,1,1])).to.be.rejected.revertedWith(
            "Student can't have more than 1 of this token"
          );
    });

    it("certificateAllocation: Transaction should be rejected if called by another student, but pass if called by owner", async function () {
        const { contract, owner, student } = await loadFixture(deploymentFunction);

        // Allocation of 1 "Presentations"-token, 1 "SmartContractProtocol"-token and 1 "Demos"-token to student
        await contract.connect(owner).mintBatch(student, [0,1,2], [1,1,1]);

        // Student tries to allocate certificate to student who does fullfill criteria for E
        await expect(contract.connect(student).certificateAllocation(student)).to.be.rejected

        // Teacher tries to allocate certificate to student who does fullfill criteria for E
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 7)).to.equal(1);
    });

    it("certificateAllocation: Transaction should be rejected if students does not qualify for certificate, else pass", async function () {
        const { contract, owner, student } = await loadFixture(deploymentFunction);

        // Teacher tries to allocate certificate although student does not fullfill criteria
        await expect(contract.connect(owner).certificateAllocation(student)).to.be.rejected.revertedWith(
            "Student must have passed mandatory tasks"
          );

        // Allocation of 1 "Presentations"-token to student
         await contract.connect(owner).mint(student, 0, 1);

        // Teacher tries to allocate certificate although student does not fullfill criteria
        await expect(contract.connect(owner).certificateAllocation(student)).to.be.rejected.revertedWith(
            "Student must have passed mandatory tasks"
          );

        // Allocation of 1 "SmartContractProtocol"-token to student
        await contract.connect(owner).mint(student, 1, 1);

        // Teacher tries to allocate certificate although student does not fullfill criteria
        await expect(contract.connect(owner).certificateAllocation(student)).to.be.rejected.revertedWith(
            "Student must have passed mandatory tasks"
        );

        // Allocation of 1 "Demos"-token to student
        await contract.connect(owner).mint(student, 2, 1);

        // Teacher tries to allocate certificate to student who does fullfill criteria for E
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 7)).to.equal(1);

        // Allocation of 1 "OpenSourceContributions"-token to student
        await contract.connect(owner).mint(student, 3, 1);

        // Teacher tries to allocate certificate to student who does fullfill criteria for D
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 8)).to.equal(1);

        // Allocation of 1 "Feedback"-token to student
        await contract.connect(owner).mint(student, 4, 1);

        // Teacher tries to allocate certificate to student who does fullfill criteria for C
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 9)).to.equal(1);

        // Allocation of 1 "Essays"-token to student
        await contract.connect(owner).mint(student, 5, 1);

        // Teacher tries to allocate certificate to student who does fullfill criteria for B
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 10)).to.equal(1);

        // Allocation of 1 "Questions"-token to student
        await contract.connect(owner).mint(student, 6, 1);

        // Teacher tries to allocate certificate to student who does fullfill criteria for A
        await contract.connect(owner).certificateAllocation(student);
        expect(await contract.balanceOf(student, 11)).to.equal(1);
    }); 

    it("Student should not be able to transfer soul bound token", async function () {
        const { contract, owner, student, student2 } = await loadFixture(deploymentFunction);

        // Prepare allocation of 1 "Questions"-token to student
        await contract.connect(owner).mint(student, 6, 1);

        // Student tries to transfer 1 "Questions"-token to student2
        await expect(contract.connect(student).safeTransferFrom(student, student2, 6, 1, "0x0")).to.be.rejected
    }); 
});
