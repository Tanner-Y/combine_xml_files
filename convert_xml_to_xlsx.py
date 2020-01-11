from xml.dom import minidom
def convert_xml_to_array(xml_path, start_row):
    xmldoc = minidom.parse(xml_path)
    itemlist=xmldoc.getElementsByTagName('Row')
    arrays = []
    i = 0
    for rows in itemlist:
        if i < start_row:
            i += 1
            continue
        row = []
        item=rows.getElementsByTagName('Cell')
        for Celle in item:
            for child in Celle.childNodes:
                try:
                    row.append((child.childNodes[0].nodeValue).title())
                except:
                    row.append("")
        arrays.append(row)
    return arrays