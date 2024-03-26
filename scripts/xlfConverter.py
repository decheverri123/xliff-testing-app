import xml.etree.ElementTree as ET
import sys
import copy


def process_xlf(input_file, output_file, prefix):
    # Parse the input XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Set the namespace map
    ET.register_namespace('', 'urn:oasis:names:tc:xliff:document:1.2')

    # Iterate over each trans-unit in the file
    for trans_unit in root.findall('.//{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
        # Get the source element
        source = trans_unit.find(
            '{urn:oasis:names:tc:xliff:document:1.2}source')

        # Create the target element
        target = ET.Element('{urn:oasis:names:tc:xliff:document:1.2}target')

        # Check for dynamic content in source
        dynamic_elements = source.findall(
            './/{urn:oasis:names:tc:xliff:document:1.2}x')
        source_starts_with_curly = source.text and source.text.startswith('{')

        if dynamic_elements and not source_starts_with_curly:
            # If dynamic content exists, copy the source element and its children to the target element
            source_text = source.text.strip() if source.text else ''
            target.text = f"{prefix}-{source_text} "
            for child in source:
                target_child = copy.deepcopy(child)
                target.append(target_child)

        elif dynamic_elements and source_starts_with_curly:
            # If dynamic content exists, copy the source element and its children to the target element
            source_text = source.text.strip() if source.text else ''
            target.text = f"{source_text}"
            for child in source:
                target_child = copy.deepcopy(child)
                target.append(target_child)
                if target_child.tail:
                    target_child.tail = f" {target_child.tail.strip()}-{prefix}"
                else:
                    target_child.tail = f" -{prefix}"

        elif source_starts_with_curly:
            source_text = source.text.strip() if source.text else ''
            target.text = ''.join(source.itertext()).strip()
            target.text += f"-{prefix} "

        else:
            # No dynamic content, apply prefix and suffix to text
            source_text = ''.join(source.itertext()).strip()
            target.text = f"{prefix}-{source_text}-{prefix}"

        # Insert the target element after the source element
        source_index = list(trans_unit).index(source)
        trans_unit.insert(source_index + 1, target)

    # Write the modified tree to the output file
    tree.write(output_file, encoding='UTF-8', xml_declaration=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py prefix input.xlf output.xlf")
        sys.exit(1)

    prefix = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    process_xlf(input_file, output_file, prefix)
