import json
import xml.etree.ElementTree as ET

def process_json(json_data):
    try:
        data = json.loads(json_data)
        print("JSON data:", data)
    except json.JSONDecodeError as e:
        print("Error processing JSON data:", e)

def process_xml(xml_data):
    try:
        tree = ET.ElementTree(ET.fromstring(xml_data))
        root = tree.getroot()
        print("XML data:")
        for child in root:
            print(child.tag, child.attrib, child.text)
    except ET.ParseError as e:
        print("Error processing XML data:", e)

# Example usage
print("Processing JSON and XML data:")
json_data = '{"name": "Keyur", "age": 21, "city": "New York"}'



xml_data = '''
<person>
    <name>Keyur</name>
    <age>21</age>
    <city>New York</city>
</person>
'''

process_json(json_data)
process_xml(xml_data)
