const { expect } = require("chai");
const hre = require("hardhat");
const { time } = require("@nomicfoundation/hardhat-toolbox/network-helpers");

describe("Eos", function () {
  it("Should set the right unlockTime", async function () {
    const lockedAmount = 1_000_000_000;
    const ONE_YEAR_IN_SECS = 365 * 24 * 60 * 60;
    const unlockTime = (await time.latest()) + ONE_YEAR_IN_SECS;

    // deploy a lock contract where funds can be withdrawn
    // one year in the future
    const eso = await hre.ethers.deployContract("EsoToken");

    // assert that the value is correct
    expect(await eso.totalSupply()).to.equal(0);
  });
});