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

    # Ensure the root element is <xliff>
    if root.tag != 'xliff':
        new_root = ET.Element('xliff')
        new_root.set('version', '1.2')
        new_root.set('xmlns', 'urn:oasis:names:tc:xliff:document:1.2')
        new_root.append(root)
        tree._setroot(new_root)

    # Add the <file> element if it doesn't exist
    file_element = root.find("./file")
    if file_element is None:
        file_element = ET.SubElement(root, 'file')
        file_element.set('source-language', 'en')
        file_element.set('datatype', 'plaintext')
        file_element.set('original', 'ng2.template')
        body_element = ET.SubElement(file_element, 'body')
        for trans_unit in trans_units:
            body_element.append(trans_unit)

    tree.write(output_file, encoding="utf-8", xml_declaration=True)


if len(sys.argv) != 4:
    print("Usage: python converter.py prefix input_file output_file")
    sys.exit(1)

prefix = sys.argv[1]
source_file = sys.argv[2]
output_file = sys.argv[3]

process_xlf_file(source_file, output_file, prefix)
print(f"Modified .xlf file has been generated: {output_file}")
