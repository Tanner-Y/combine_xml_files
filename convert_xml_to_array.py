from xml.dom import minidom
def xml_to_array(xml_path, start_row):
    xmldoc = minidom.parse(xml_path)
    itemlist=xmldoc.getElementsByTagName('Row')
    arrays = []
    i = 0
    # Thank you to P.Brt on stackoverflow for the skeleton of this code
    # https://stackoverflow.com/questions/46561349/import-an-xml-file-generated-by-excel-in-python?newreg=5b767cb6e49d43929a1a067992fbe8b8
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