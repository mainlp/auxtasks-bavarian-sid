#!/usr/bin/python3

import sys
import os
import json
import pandas as pd

def json2csv(output_csv_directory, input_json_file, output_type):

    if not os.path.exists(output_csv_directory):
        os.makedirs(output_csv_directory)

    with open(input_json_file, 'r') as file:
        data = json.load(file)

    for key in data:
        if key == output_type:
            df = pd.DataFrame.from_dict(data[key], orient='index').transpose()

            output_csv_file = os.path.join(output_csv_directory, f'{out_name}_{key}.csv')
            df.to_csv(output_csv_file, index=False, na_rep='')

    print(f"{output_type} csv file for {input_json_file} successfully created.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: json2csv.py <input_json_file> <output_csv_directory> <output_type>")
        print("possible output types: all | baseline | dialects")
        sys.exit(1)

    input_json_file = sys.argv[1]
    out_name = input_json_file.split('/')[-1]
    out_name = out_name.replace('.json', '')
    output_csv_directory = sys.argv[2]
    output_type = sys.argv[3]

    json2csv(output_csv_directory, input_json_file, output_type)
