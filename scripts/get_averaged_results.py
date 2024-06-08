#!/usr/bin/python3

import os
import json
from collections import defaultdict


def get_matching_experiments(results_directory):
    experiments_files = defaultdict(list)

    for file in os.listdir(results_directory):
        if os.path.isfile(os.path.join(results_directory, file)):
            if '_' in file:
                prefix, suffix = file.rsplit('_', 1)
                experiments_files[prefix].append(file)
    return experiments_files


def calculate_average(values_list):
    if not values_list:
        return 0
    flattened_list = [item for sublist in values_list for item in sublist]
    return round(sum(flattened_list) / len(flattened_list), 1) if flattened_list else 0


def merge_json_data(json_data_list):
    merged_data = {
        "all": {"Language": [], "slots": defaultdict(list), "intents": defaultdict(list), "fully correct": defaultdict(list)},
        "baseline": {"Language": [], "slots": defaultdict(list), "intents": defaultdict(list), "fully correct": defaultdict(list)},
        "dialects": {"Language": [], "slots": defaultdict(list), "intents": defaultdict(list), "fully correct": defaultdict(list)}
    }

    for data in json_data_list:
        for category in ["all", "baseline", "dialects"]:
            if not merged_data[category]["Language"]:
                merged_data[category]["Language"] = data[category]["Language"]
            for i, lang in enumerate(data[category]["Language"]):
                merged_data[category]["slots"][lang].append(data[category]["slots"][i])
                merged_data[category]["intents"][lang].append(data[category]["intents"][i])
                merged_data[category]["fully correct"][lang].append(data[category]["fully correct"][i])

    def get_averages_for_category(category_data, langs2average):
        averaged_slots = [calculate_average([category_data["slots"][lang]]) for lang in category_data["Language"]]
        averaged_intents = [calculate_average([category_data["intents"][lang]]) for lang in category_data["Language"]]
        averaged_fully_correct = [calculate_average([category_data["fully correct"][lang]]) for lang in category_data["Language"]]

        avg_slots = calculate_average([category_data["slots"][lang] for lang in langs2average if lang in category_data["slots"]])
        avg_intents = calculate_average([category_data["intents"][lang] for lang in langs2average if lang in category_data["intents"]])
        avg_fully_correct = calculate_average([category_data["fully correct"][lang] for lang in langs2average if lang in category_data["fully correct"]])

        return averaged_slots, averaged_intents, averaged_fully_correct, avg_slots, avg_intents, avg_fully_correct

    # Define languages to average for each category
    all_langs2average = ['ar', 'da', 'de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw', 'id', 'it', 'ja', 'kk', 'lt', 'nap', 'nl', 'sr', 'tr', 'zh']
    base_langs2average = ['de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja']
    dial_langs2average = ['de-st', 'de-ba', 'de-by']

    # Get averages for all categories
    all_slots, all_intents, all_fully_correct, avg_all_slots, avg_all_intents, avg_all_fully_correct = get_averages_for_category(merged_data["all"], all_langs2average)
    baseline_slots, baseline_intents, baseline_fully_correct, avg_baseline_slots, avg_baseline_intents, avg_baseline_fully_correct = get_averages_for_category(merged_data["baseline"], base_langs2average)
    dialects_slots, dialects_intents, dialects_fully_correct, avg_dialects_slots, avg_dialects_intents, avg_dialects_fully_correct = get_averages_for_category(merged_data["dialects"], dial_langs2average)

    averaged_data = {
        "all": {
            "Language": merged_data["all"]["Language"] + ["Avg."],
            "slots": all_slots + [avg_all_slots],
            "intents": all_intents + [avg_all_intents],
            "fully correct": all_fully_correct + [avg_all_fully_correct],
        },
        "baseline": {
            "Language": merged_data["baseline"]["Language"] + ["Avg."],
            "slots": baseline_slots + [avg_baseline_slots],
            "intents": baseline_intents + [avg_baseline_intents],
            "fully correct": baseline_fully_correct + [avg_baseline_fully_correct],
        },
        "dialects": {
            "Language": merged_data["dialects"]["Language"] + ["Avg."],
            "slots": dialects_slots + [avg_dialects_slots],
            "intents": dialects_intents + [avg_dialects_intents],
            "fully correct": dialects_fully_correct + [avg_dialects_fully_correct],
        }
    }

    return averaged_data


def read_matching_files(directory, experiments_files):
    for prefix, filenames in experiments_files.items():
        json_data_list = []

        for filename in filenames:
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r') as file:
                data = json.load(file)
                json_data_list.append(data)

        averaged_data = merge_json_data(json_data_list)

        output_filename = f"{prefix}.json"
        output_filepath = os.path.join(directory, output_filename)

        with open(output_filepath, 'w') as output_file:
            json.dump(averaged_data, output_file, indent=4)


if __name__ == "__main__":
    # for local testing in pycharm
    directory = 'results_test/'

    # for testing in Colab and with access to drive:
    # directory = '/content/drive/MyDrive/Masterarbeit/results/'

    experiments_files = get_matching_experiments(directory)
    read_matching_files(directory, experiments_files)
