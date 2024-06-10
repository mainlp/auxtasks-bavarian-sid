#!/usr/bin/python3

import json
import pandas as pd
import sys
import os
import numpy as np


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        # Todo: add argument to say if all, baseline or dialects output should be created
        print("Usage: script.py <input_json_file> <output_csv_directory>")
        sys.exit(1)

    input_json_file = sys.argv[1]
    out_name = input_json_file.split('/')[-1]
    out_name = out_name.replace('.json', '')
    output_csv_directory = sys.argv[2]

    # Ensure the output directory exists
    if not os.path.exists(output_csv_directory):
        os.makedirs(output_csv_directory)

    # Load the JSON data from a file
    with open(input_json_file, 'r') as file:
        data = json.load(file)

    # Convert each section of the JSON to a DataFrame and save as a CSV file
    for key in data:
        # Normalizing the data and filling missing slots with NaN
        df = pd.DataFrame.from_dict(data[key], orient='index').transpose()

        # Save the DataFrame as a CSV file
        output_csv_file = os.path.join(output_csv_directory, f'{out_name}_{key}.csv')
        df.to_csv(output_csv_file, index=False, na_rep='')

    print("CSV files created successfully.")


if __name__ == "__main__":
    main()
