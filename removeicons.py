import xml.etree.ElementTree as ET
import xml.dom.minidom

# Path to the XML file
xml_file_path = r'C:\epg\utc.xml'

# Parse the XML file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Iterate through each channel element
for channel_elem in root.findall('.//channel'):
    # Remove the icon element from each channel
    for icon_elem in channel_elem.findall('icon'):
        channel_elem.remove(icon_elem)

# Convert the modified XML to a string with prettified formatting
xml_string = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()

# Remove empty lines from the XML string
xml_string = '\n'.join([line for line in xml_string.split('\n') if line.strip()])

# Write the modified XML back to the file with utf-8 encoding
with open(xml_file_path, 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_string)

print(f"XML file at {xml_file_path} has been modified with proper indentation.")
