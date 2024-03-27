// scripts/test.js

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

// Get the list of script files in the "scripts" folder
const scriptFiles = fs
  .readdirSync(__dirname)
  .filter((file) => file.endsWith(".js") && file !== "runNodeTests.js");

// Run each script file
scriptFiles.forEach((file) => {
  const scriptFile = path.join(__dirname, file);
  console.log(`Running script: ${file}`);
  execSync(`node ${scriptFile}`, { stdio: "inherit" });
});
