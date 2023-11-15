import requests
import gzip
import xml.etree.ElementTree as ET
import xml.dom.minidom
import os

# URL for the gzipped XML file
url = 'https://epg.tvnow.best/utc.xml.gz'

# Path for the local XML file
local_xml_file_path = r'C:\epg\utc.xml'

# Path for the local gzipped XML file
local_gzipped_xml_file_path = r'C:\epg\utc.xml.gz'

# Download the gzipped XML file
response = requests.get(url)
if response.status_code == 200:
    # Save the gzipped content to a local file
    with open(local_gzipped_xml_file_path, 'wb') as f:
        f.write(response.content)

    # Extract the gzipped file
    with gzip.open(local_gzipped_xml_file_path, 'rb') as f_in, open(local_xml_file_path, 'wb') as f_out:
        f_out.write(f_in.read())

    # Remove the gzipped file after extraction
    os.remove(local_gzipped_xml_file_path)

    # Parse the XML file
    tree = ET.parse(local_xml_file_path)
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
    with open(local_xml_file_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_string)

    print(f"XML file at {local_xml_file_path} has been modified with proper indentation.")
else:
    print(f"Failed to download the file from {url}. Status code: {response.status_code}")
