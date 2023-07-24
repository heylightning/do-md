# prototype/nextMove.txt

import xml.etree.ElementTree as ET

def tableDataConfig(block_xml):
    columns = []
    rows = []
    root = ET.fromstring(block_xml)

    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    for col in root.findall(".//w:gridCol", namespaces=namespaces):
        columns.append('found col')
    
    for row in root.findall(".//w:tr", namespaces=namespaces):
        row_names = []
        for cell in row.findall('.//w:t', namespaces=namespaces):
            print(cell.text.strip())
            row_names.append(cell.text.strip())
        rows.append(row_names)
    
    return columns, rows
