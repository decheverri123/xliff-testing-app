# Automated Testing

## XLIFF

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

### Running tests

`node scripts/translationCompletenessCheck.js`

### Starting app in French
`npm run start:fr`
