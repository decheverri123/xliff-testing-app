const fs = require("fs");
const path = require("path");
const xml2js = require("xml2js");

const parseXlfFile = (filePath) => {
  const content = fs.readFileSync(filePath, "utf8");
  return new Promise((resolve, reject) => {
    xml2js.parseString(content, (err, result) => {
      if (err) reject(err);
      else
        resolve(
          result.xliff.file[0]["body"][0]["trans-unit"].map((unit) => unit.$.id)
        );
    });
  });
};

const compareTranslations = async (baseFilePath, targetFilePath) => {
  const baseIds = await parseXlfFile(baseFilePath);
  const targetIds = await parseXlfFile(targetFilePath);

  const missingInTarget = baseIds.filter((id) => !targetIds.includes(id));
  const extraInTarget = targetIds.filter((id) => !baseIds.includes(id));

  if (missingInTarget.length > 0) {
    console.log(
      `Missing translations from ${baseFilePath} to ${targetFilePath}:`,
      missingInTarget
    );
  }
  if (extraInTarget.length > 0) {
    console.log(
      `Extra translations from ${baseFilePath} to ${targetFilePath}:`,
      extraInTarget
    );
  }

  if (missingInTarget.length === 0 && extraInTarget.length === 0) {
    console.log(
      `All translations between ${baseFilePath} and ${targetFilePath} are complete!`
    );
  }
};

const localeDir = "src/locale";
const xlfFiles = fs
  .readdirSync(localeDir)
  .filter((file) => file.endsWith(".xlf"));

xlfFiles.forEach((baseFile, index) => {
  for (let i = index + 1; i < xlfFiles.length; i++) {
    const targetFile = xlfFiles[i];
    const basePath = path.join(localeDir, baseFile);
    const targetPath = path.join(localeDir, targetFile);
    compareTranslations(basePath, targetPath).catch(console.error);
  }
});
