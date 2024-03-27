# Automated Testing

## Types of Testing for XLIFF

### Structural Validation

- Validate the structure and syntax of the XLIFF files against the XLIFF schema or specification.
- Ensure that the XLIFF files are well-formed XML documents and adhere to the XLIFF format.
- Check for missing or incorrect elements, attributes, or tags.
- Verify that the structure of the XLIFF files is consistent across all languages.

### Completeness Check

- Verify that all translatable units (`<trans-unit>`) from the source language are present in the translated XLIFF files.
- Check for missing translations or untranslated content.
- Ensure that all required elements and attributes are present for each translation unit.

### Placeholder Consistency

- Check that placeholders (e.g., `{0}`, `{1}`) used in the source text are correctly preserved in the translations.
- Verify that the placeholders are used consistently and have not been modified or removed in the translated text.

### Character Encoding and Special Characters

- Validate that the XLIFF files use the correct character encoding (e.g., UTF-8).
- Check for any issues with special characters, such as non-ASCII characters or escaped entities.
- Ensure that special characters are properly handled and displayed in the translations.

### Length Validation

- Compare the length of the translated text against the source text.
- Check for translations that are significantly shorter or longer than the source text, which may indicate truncation or excessive expansion.
- Define acceptable length thresholds and flag translations that exceed or fall below those thresholds.

### Integration Testing

- Perform integration testing by loading the translated XLIFF files into your application or localization framework.
- Verify that the translations are correctly displayed and functioning as expected within the application. Check for any layout or formatting issues caused by the translations.

### Continuous Integration and Continuous Delivery (CI/CD)

- Incorporate the automated testing of XLIFF files into your CI/CD pipeline.
- Run the tests automatically whenever changes are made to the XLIFF files or when new translations are added.
- Ensure that the tests are executed before deploying the application to catch any localization issues early in the development process.

### Running tests (only one completed as example)

`node scripts/translationCompletenessCheck.js`

### Starting app in English

`npm run start`

### Starting app in French

`npm run start:fr`

### Starting app in Spanish

`npm run start:es`

### Starting app using auto-generated .xfl

`npm run start:xx`

## Python XLF Generation Script Documentation

### Introduction

This Python script is designed to process XLF (XML Localization Interchange File Format) files. It modifies the content of `<source>` elements by appending or prepending a specified prefix and creating corresponding `<target>` elements within each `<trans-unit>` element of the XLF file.

### Features

- **Prefix Application**: Adds a specified prefix to the text within `<source>` elements.
- **Dynamic Content Handling**: Detects and handles dynamic content (e.g., placeholders or special XML tags) differently to avoid altering their structure.
- **Element Duplication**: Copies the entire structure of `<source>` elements into `<target>` elements, preserving any nested XML.

### How It Works

1. **Parsing the XLF File**: The script uses `ElementTree` to parse the XLF file and iterates through each `trans-unit` element.
2. **Content Analysis**: Determines whether the `<source>` element contains dynamic content (like placeholders or special XML tags).
3. **Content Duplication and Modification**:
   - If dynamic content is detected, the script copies this content as-is into the `<target>` element, optionally adding the prefix outside of the dynamic content.
   - If no dynamic content is present, the script wraps the entire text of the `<source>` element with the specified prefix and suffix.
4. **Target Element Creation**: A `<target>` element is created within each `trans-unit`, containing the modified content.
5. **Output Generation**: The modified XML tree is written to a new XLF file.

### Usage Instructions

### Prerequisites

- Python installed on your system.
- The XLF file to be processed.

### Running the Script

1. Place the script in the same directory as the XLF file to be processed or ensure the script can access the file path.
2. Use the command line to navigate to the script's directory.
3. Run the script with the following command format:

```bash
python script.py [prefix] [input.xlf] [output.xlf]
```

- `[prefix]`: The text to prepend or append to the content within `<source>` elements.
- `[input.xlf]`: The path to the input XLF file.
- `[output.xlf]`: The desired path for the output XLF file.

### Example Command

```bash
python script.py "xx-" source.xlf modified.xlf 
```

This command will process source.xlf, adding "xx-" before and after the text content in `<source>` elements (if the content does not start with '{' or contain dynamic elements), and save the modified content to modified.xlf.

Notes
The script intelligently handles dynamic content, ensuring that placeholders and special XML structures are preserved and not mistakenly altered by the prefix or suffix.

The output file will be overwritten if it already exists, so ensure that you use the correct file name to avoid accidental data loss.
