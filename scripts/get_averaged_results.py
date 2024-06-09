#!/usr/bin/python3

import os
import json
import math
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

def calculate_standard_deviation(values_list):
    if not values_list:
        return 0
    flattened_list = [item for sublist in values_list for item in sublist]
    if not flattened_list:
        return 0
    mean = sum(flattened_list) / len(flattened_list)
    variance = sum((x - mean) ** 2 for x in flattened_list) / len(flattened_list)
    return round(math.sqrt(variance), 1)

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

    def get_runs_average(category_data):
        # calculate the average over the different random seed runs
        averaged_slots = [calculate_average([category_data["slots"][lang]]) for lang in category_data["Language"]]
        averaged_intents = [calculate_average([category_data["intents"][lang]]) for lang in category_data["Language"]]
        averaged_fully_correct = [calculate_average([category_data["fully correct"][lang]]) for lang in category_data["Language"]]
        return averaged_slots, averaged_intents, averaged_fully_correct


    def get_average_for_langs(category_data, langs2average):
        # calculate the average for the averaged runs depending on respective languages
        avg_slots = calculate_average([category_data["slots"][lang] for lang in langs2average if lang in category_data["slots"]])
        avg_intents = calculate_average([category_data["intents"][lang] for lang in langs2average if lang in category_data["intents"]])
        avg_fully_correct = calculate_average([category_data["fully correct"][lang] for lang in langs2average if lang in category_data["fully correct"]])

        return avg_slots, avg_intents, avg_fully_correct

    def get_diff2baseline(category_data, langs2average, mode=None):
        # calculate the difference of the averaged random seeds run to the averaged baseline rund with mDeBERTa
        baseline_all_slots_avg = 63.4
        baseline_all_intents_avg = 83.4
        baseline_all_fully_avg = 43.4
        baseline_base_slots_avg = 76.6
        baseline_base_intents_avg = 86.6
        baseline_base_fully_avg = 46.6
        baseline_dial_slots_avg = 70.4
        baseline_dial_intents_avg = 60.4
        baseline_dial_fully_avg = 34.4

        if mode == "all":
            diff_slots = round(calculate_average([category_data["slots"][lang] for lang in langs2average if lang in category_data["slots"]]) - baseline_all_slots_avg, 1)
            diff_intents = round(calculate_average([category_data["intents"][lang] for lang in langs2average if lang in category_data["intents"]]) - baseline_all_intents_avg, 1)
            diff_fully_correct = round(calculate_average([category_data["fully correct"][lang] for lang in langs2average if lang in category_data["fully correct"]]) - baseline_all_fully_avg, 1)
            return diff_slots, diff_intents, diff_fully_correct

        elif mode == "baseline":
            diff_slots = round(calculate_average([category_data["slots"][lang] for lang in langs2average if lang in category_data["slots"]]) - baseline_base_slots_avg, 1)
            diff_intents = round(calculate_average([category_data["intents"][lang] for lang in langs2average if lang in category_data["intents"]]) - baseline_base_intents_avg, 1)
            diff_fully_correct = round(calculate_average([category_data["fully correct"][lang] for lang in langs2average if lang in category_data["fully correct"]]) - baseline_base_fully_avg, 1)
            return diff_slots, diff_intents, diff_fully_correct

        elif mode == "dialects":
            diff_slots = round(calculate_average([category_data["slots"][lang] for lang in langs2average if lang in category_data["slots"]]) - baseline_dial_slots_avg, 1)
            diff_intents = round(calculate_average([category_data["intents"][lang] for lang in langs2average if lang in category_data["intents"]]) - baseline_dial_intents_avg, 1)
            diff_fully_correct = round(calculate_average([category_data["fully correct"][lang] for lang in langs2average if lang in category_data["fully correct"]]) - baseline_dial_fully_avg, 1)
            return diff_slots, diff_intents, diff_fully_correct

    def get_standard_deviation(category_data):
        # calculate the standard deviation over the different random seed runs
        sd_slots = [calculate_standard_deviation([category_data["slots"][lang]]) for lang in category_data["Language"]]
        sd_intents = [calculate_standard_deviation([category_data["intents"][lang]]) for lang in category_data["Language"]]

        return sd_slots, sd_intents


    # Get the average over the different random seed runs
    all_slots, all_intents, all_fully_correct = get_runs_average(merged_data["all"])
    baseline_slots, baseline_intents, baseline_fully_correct = get_runs_average(merged_data["baseline"])
    dialects_slots, dialects_intents, dialects_fully_correct = get_runs_average(merged_data["dialects"])

    # Define languages to average for each category
    all_langs2average = ['ar', 'da', 'de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw', 'id', 'it', 'ja', 'kk', 'lt', 'nap', 'nl', 'sr', 'tr', 'zh']
    base_langs2average = ['de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja']
    dial_langs2average = ['de-st', 'de-ba', 'de-by']

    # Get the average for the averaged runs depending on respective languages
    avg_all_slots, avg_all_intents, avg_all_fully_correct = get_average_for_langs(merged_data["all"], all_langs2average)
    avg_baseline_slots, avg_baseline_intents, avg_baseline_fully_correct = get_average_for_langs(merged_data["baseline"], base_langs2average)
    avg_dialects_slots, avg_dialects_intents, avg_dialects_fully_correct = get_average_for_langs(merged_data["dialects"], dial_langs2average)

    # Get the standard deviation over the different random seed runs
    sd_all_slots, sd_all_intents = get_standard_deviation(merged_data["all"])
    sd_baseline_slots, sd_baseline_intents = get_standard_deviation(merged_data["baseline"])
    sd_dialects_slots, sd_dialects_intents = get_standard_deviation(merged_data["dialects"])

    # Get the difference between this average and the baseline average
    diff_all_slots, diff_all_intents, diff_all_fully = get_diff2baseline(merged_data["all"], all_langs2average, mode="all")
    diff_base_slots, diff_base_intents, diff_base_fully = get_diff2baseline(merged_data["all"], all_langs2average, mode="baseline")
    diff_dial_slots, diff_dial_intents, diff_dial_fully = get_diff2baseline(merged_data["all"], all_langs2average, mode="dialects")

    averaged_data = {
        "all": {
            "Language": merged_data["all"]["Language"] + ["Avg."] + ["Diff."],
            "slots": all_slots + [avg_all_slots] + [diff_all_slots],
            "intents": all_intents + [avg_all_intents] + [diff_all_intents],
            "fully correct": all_fully_correct + [avg_all_fully_correct] + [diff_all_fully],
            "sd slots": sd_all_slots,
            "sd intents": sd_all_intents
        },
        "baseline": {
            "Language": merged_data["baseline"]["Language"] + ["Avg."] + ["Diff."],
            "slots": baseline_slots + [avg_baseline_slots] + [diff_base_slots],
            "intents": baseline_intents + [avg_baseline_intents] + [diff_base_intents],
            "fully correct": baseline_fully_correct + [avg_baseline_fully_correct] + [diff_base_fully],
            "sd slots": sd_baseline_slots,
            "sd intents": sd_baseline_intents
        },
        "dialects": {
            "Language": merged_data["dialects"]["Language"] + ["Avg."] + ["Diff."],
            "slots": dialects_slots + [avg_dialects_slots] + [diff_dial_slots],
            "intents": dialects_intents + [avg_dialects_intents] + [diff_dial_intents],
            "fully correct": dialects_fully_correct + [avg_dialects_fully_correct] + [diff_dial_fully],
            "sd slots": sd_dialects_slots,
            "sd intents": sd_dialects_intents
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
