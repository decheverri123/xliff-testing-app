import sys
import xml.etree.ElementTree as ET


def process_xlf_file(source_file, output_file, prefix):
    tree = ET.parse(source_file)
    root = tree.getroot()

    # Remove the namespace prefix from all elements
    for elem in root.iter():
        if elem.tag.startswith('{'):
            elem.tag = elem.tag.split('}', 1)[1]

    # Find all <trans-unit> elements
    trans_units = root.findall(".//trans-unit")

    for trans_unit in trans_units:
        source_element = trans_unit.find("./source")
        if source_element is not None:
            source_text = source_element.text
            modified_text = f"{prefix}-{source_text}-{prefix}"
            source_element.text = modified_text

    tree.write(output_file, encoding="utf-8", xml_declaration=True)


if len(sys.argv) != 4:
    print("Usage: python converter.py prefix input_file output_file")
    sys.exit(1)

prefix = sys.argv[1]
source_file = sys.argv[2]
output_file = sys.argv[3]

process_xlf_file(source_file, output_file, prefix)
print(f"Modified .xlf file has been generated: {output_file}")
