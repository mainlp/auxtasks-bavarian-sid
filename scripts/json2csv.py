#!/usr/bin/python3

import json
import pandas as pd
import sys
import os

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: script.py <input_json_file> <output_csv_directory>")
        sys.exit(1)

    input_json_file = sys.argv[1]
    output_csv_directory = sys.argv[2]

    # Ensure the output directory exists
    if not os.path.exists(output_csv_directory):
        os.makedirs(output_csv_directory)

    # Load the JSON data from a file
    with open(input_json_file, 'r') as file:
        data = json.load(file)

    # Convert each section of the JSON to a DataFrame and save as a CSV file
    for key in data:
        df = pd.DataFrame(data[key])
        output_csv_file = os.path.join(output_csv_directory, f'{key}.csv')
        df.to_csv(output_csv_file, index=False)

    print("CSV files created successfully.")

if __name__ == "__main__":
    main()
