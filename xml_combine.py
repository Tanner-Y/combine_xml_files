import os
import sys
from convert_xml_to_array import xml_to_array
import csv

def xml_combiner(input_dir='input', output_dir='output'):
    try:
        directory = os.fsencode(input_dir)
    except Exception as e:
        print(f"Directory path {input_dir} is invalid. Error: {e}")
        return e
    i = 0
    j = 0
    r = 0
    start_row = 0 # If all spreadsheets have the same first row, ignore further headers
    output = []
    for file in os.listdir(directory):
        i += 1
        print("Parsing file: " + str(i))
        filename = os.fsdecode(file)
        try:
            curr_array = (xml_to_array(f"{input_dir}/{filename}",start_row))
            for row in curr_array:
                output.append(row)
                r += 1
            j += 1
        except Exception as e:
            print(f"Unexpected error. Failed on file: {filename} - sorry. Error code: {e}")
        start_row = 1 # If all spreadsheets have the same first row, ignore further headers
    print(f"Complete. Added {r} rows from {j} of {i} files in {os.fsdecode(directory)}.")
    with open(f"{output_dir}/out.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(output)

if __name__ == "__main__":
    try:
        xml_combiner(sys.argv[-1], sys.argv[-1])
    except:
        try:
            xml_combiner(sys.argv[-1])
        except:
            xml_combiner()