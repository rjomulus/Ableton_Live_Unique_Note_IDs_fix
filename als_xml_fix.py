import sys
import gzip
import xml.etree.ElementTree as ET
from io import StringIO
import asyncio

class CorruptionType:
    DUPLICATE_NOTE_IDS = 1

def decompress_als(file_path):
    with gzip.open(file_path, 'rb') as f:
        xml_content = f.read()
    return xml_content

def compress_als(xml_content, output_path):
    with gzip.open(output_path, 'wb') as f:
        f.write(xml_content)

def parse_xml(xml_content):
    return ET.ElementTree(ET.fromstring(xml_content))

def save_xml(tree):
    string_io = StringIO()
    tree.write(string_io, encoding='unicode', xml_declaration=True)
    return string_io.getvalue().encode('utf-8')

def run_duplicate_note_ids_algorithm(root):
    note_ids = {}
    new_id = 99990

    for elem in root.iter():
        note_id = elem.attrib.get('NoteId')
        if note_id:
            if note_id in note_ids:
                # Assign a new unique NoteId
                elem.attrib['NoteId'] = str(new_id)
                new_id += 1
            else:
                note_ids[note_id] = elem

async def fix_corrupt_als_async(file_path, corruption_type, ff_key_tracks):
    xml_content = decompress_als(file_path)
    xml_tree = parse_xml(xml_content)
    root = xml_tree.getroot()

    if corruption_type == CorruptionType.DUPLICATE_NOTE_IDS:
        run_duplicate_note_ids_algorithm(root)

    xml_string = save_xml(xml_tree)
    compress_als(xml_string, 'output_file_fixed.als')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_als_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fix_corrupt_als_async(file_path, CorruptionType.DUPLICATE_NOTE_IDS, True))
    print("ALS file has been fixed and saved as 'output_file_fixed.als'")
