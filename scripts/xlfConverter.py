import sys
import xml.etree.ElementTree as ET


def process_xlf_file(source_file, output_file, prefix):
    # Parse the source .xlf file
    tree = ET.parse(source_file)
    root = tree.getroot()

    # Get the namespace URI
    namespace = {'ns': root.tag.split('}')[0].strip('{')}

    # Find all <trans-unit> elements
    trans_units = root.findall(".//ns:trans-unit", namespace)

    # Process each <trans-unit> element
    for trans_unit in trans_units:
        source_element = trans_unit.find("./ns:source", namespace)
        if source_element is not None:
            # Modify the text content of the <source> element
            source_text = source_element.text
            modified_text = f"{prefix}-{source_text}-{prefix}"
            source_element.text = modified_text

    # Write the modified XML to the output file
    tree.write(output_file, encoding="utf-8", xml_declaration=True)


# Check if the required command-line arguments are provided
if len(sys.argv) != 4:
    print("Usage: python converter.py prefix input_file output_file")
    sys.exit(1)

# Get the source and output file paths from command-line arguments
prefix = sys.argv[1]
source_file = sys.argv[2]
output_file = sys.argv[3]

# Process the .xlf file
process_xlf_file(source_file, output_file, prefix)
print(f"Modified .xlf file has been generated: {output_file}")
