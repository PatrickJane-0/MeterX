// This setup uses Hardhat Ignition to manage smart contract deployments.
// Learn more about it at https://hardhat.org/ignition

const { buildModule } = require("@nomicfoundation/hardhat-ignition/modules");

const ONE_GWEI = 1_000_000_000n;

module.exports = buildModule("MeterXModule", (m) => {
  const lockedAmount = m.getParameter("lockedAmount", ONE_GWEI);

  const eso = m.contract("EsoToken");

  return { eso };
});
