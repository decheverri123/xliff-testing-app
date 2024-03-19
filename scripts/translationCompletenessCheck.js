const fs = require("fs");
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
    console.log("Missing translations in target:", missingInTarget);
  }
  if (extraInTarget.length > 0) {
    console.log("Extra translations in target:", extraInTarget);
  }

  if (missingInTarget.length === 0 && extraInTarget.length === 0) {
    console.log("Translations are complete!");
  }
};

// Example usage
const basePath = "src/locale/messages.xlf";
const targetPath = "src/locale/messages.fr.xlf";

compareTranslations(basePath, targetPath).catch(console.error);
