import os
from convert_xml_to_array import xml_to_array
import csv

directory = os.fsencode(dir_path)
i = 0
j = 0
r = 0
start_row = 0
output = []
for file in os.listdir(directory):
    i += 1
    print("Parsing file: " + str(i))
    filename = os.fsdecode(file)
    try:
        curr_array = (xml_to_array(f"{dir_path}/{filename}",start_row))
        for row in curr_array:
            output.append(row)
            r += 1
        j += 1
    except Exception as e:
        print(f"Unexpected error. Failed on file: {filename} - sorry. Error code: {e}")
    start_row = 1
print(f"Complete. Added {r} rows from {j} of {i} files in {os.fsdecode(directory)}.")

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)