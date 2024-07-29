#!/usr/bin/python3

import statistics

# a quick script that calculates the average numbers and standard deviations
# for the retrospectively evaluated natural Bavarian data

def calculate_stats(name, values):
    avg = sum(values) / len(values)

    std_dev = statistics.stdev(values)

    print(f"Data: {name}")
    print(f"Average: {avg:.1f}")
    print(f"Standard Deviation: {std_dev:.1f}")
    print("\n ---------------------------------------\n")


# baseline
#de-ba-nat
calculate_stats("base_nat_slots", [33.5, 32.5, 29.1])
calculate_stats("base_nat_intents", [59.6, 62.4, 60.5])
calculate_stats("base_nat_fully_correct", [13.7, 14.0, 11.1])

# de-ba-MAS
calculate_stats("base_MAS_slots", [23.7, 21.0, 21.5])
calculate_stats("base_MAS_intents", [59.2, 52.5, 54.0])
calculate_stats("base_MAS_fully_correct", [6.5, 7.8, 5.9])

# de-ba-xMAS
calculate_stats("base_xMAS_slots", [29.4, 31.2, 30.4])
calculate_stats("base_xMAS_intents", [59.8, 59.7, 61.4])
calculate_stats("base_xMAS_fully_correct", [8.8, 10.4, 8.2])

# mlmnernlu
#de-ba-nat
calculate_stats("mlmnernlu_nat_slots", [39.9, 43.9, 43.2])
calculate_stats("mlmnernlu_nat_intents", [56.7, 64.3, 62.1])
calculate_stats("mlmnernlu_nat_fully_correct", [20.7, 21.3, 18.8])

# de-ba-MAS
calculate_stats("mlmnernlu_MAS_slots", [30.1, 31.3, 29.6])
calculate_stats("mlmnernlu_MAS_intents", [51.0, 54.3, 56.0])
calculate_stats("mlmnernlu_MAS_fully_correct", [9.7, 10.7, 11.3])

# de-ba-xMAS
calculate_stats("mlmnernlu_xMAS_slots", [39.9, 40.3, 39.0])
calculate_stats("mlmnernlu_xMAS_intents", [59.1, 60.7, 62.5])
calculate_stats("mlmnernlu_xMAS_fully_correct", [13.8, 15.4, 15.5])


# mlmner_nlu
#de-ba-nat
calculate_stats("mlmner_nlu_nat_slots", [43.5, 42.0, 38.7])
calculate_stats("mlmner_nlu_nat_intents", [67.5, 66.2, 68.8])
calculate_stats("mlmner_nlu_nat_fully_correct", [21.0, 20.4, 19.1])

# de-ba-MAS
calculate_stats("mlmner_nlu_MAS_slots", [31.1, 31.3, 33.6])
calculate_stats("mlmner_nlu_MAS_intents", [59.9, 61.4, 59.0])
calculate_stats("mlmner_nlu_MAS_fully_correct", [12.4, 12.8, 12.1])

# de-ba-xMAS
calculate_stats("mlmner_nlu_xMAS_slots", [41.1, 39.3, 39.1])
calculate_stats("mlmner_nlu_xMAS_intents", [66.5, 66.0, 66.2])
calculate_stats("mlmner_nlu_xMAS_fully_correct", [17.1, 16.3, 14.9])