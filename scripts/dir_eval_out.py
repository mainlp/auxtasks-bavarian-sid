#!/usr/bin/python3

import os, sys
import json
from typing import List, Tuple, Set
from sklearn.metrics import accuracy_score, precision_recall_fscore_support


def readNlu(path):
    slots = []
    intents = []
    curSlots = []
    for line in open(path):
        line = line.strip()
        if line.startswith('# intent: '):
            intents.append(line[10:])
        if line == '':
            slots.append(curSlots)
            curSlots = []
        elif line[0] == '#' and len(line.split('\t')) == 1:
            continue
        else:
            curSlots.append(line.split('\t')[-1])
    return slots, intents

def toSpans(tags):
    spans = set()
    for beg in range(len(tags)):
        if tags[beg][0] == 'B':
            end = beg
            for end in range(beg+1, len(tags)):
                if tags[end][0] != 'I':
                    break
            spans.add(str(beg) + '-' + str(end) + ':' + tags[beg][2:])
    return spans

def getBegEnd(span):
    return [int(x) for x in span.split(':')[0].split('-')]

def getLooseOverlap(spans1, spans2):
    found = 0
    for spanIdx, span in enumerate(spans1):
        spanBeg, spanEnd = getBegEnd(span)
        label = span.split(':')[1]
        match = False
        for span2idx, span2 in enumerate(spans2):
            span2Beg, span2End = getBegEnd(span2)
            label2 = span2.split(':')[1]
            if label == label2:
                if span2Beg >= spanBeg and span2Beg <= spanEnd:
                    match = True
                if span2End <= spanEnd and span2End >= spanBeg:
                    match = True
        if match:
            found += 1
    return found

def getUnlabeled(spans1, spans2):
    return len(set([x.split('-')[0] for x in spans1]).intersection([x.split('-')[0] for x in spans2]))


def writeResults(all_langs, baseline, dialects, experiment_name):
    # Todo: find better solution here? e.g. more possible paths where to save to?
    # in colab this will be deleted when connection to runtime is quit ->
    # built in a copy command into script.sh to copy results to drive - path  does not work there

    results_dir = "/content/BaySIDshot/results/"

    # for local testing in pycharm:
    #results_dir = "/Users/xavermariakrueckl/PycharmProjects/BaySIDshot/results/"

    if not os.path.exists(results_dir):
        os.makedirs(results_dir)

    results_file_path = str(f"{results_dir}{experiment_name}.json")

    with open(results_file_path, "w", encoding="utf-8") as file:
        experiment_name = {
            "all": all_langs,
            "baseline": baseline,
            "dialects": dialects
        }
        json.dump(experiment_name, file, indent=2)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <gold_directory> <pred_directory>")
        sys.exit(1)

    gold_dir = sys.argv[1]
    pred_dir = sys.argv[2]
    # Todo: Logic here also still does not really fit
    experiment_name = str(sys.argv[2])
    experiment_name = experiment_name.split('/')[-1]
    if "predictions_" in experiment_name:
        experiment_name = experiment_name.replace("predictions_", "")
    print("Experiment Name: ", experiment_name)

    # predictiong only for test files - could be adapted to validation files here
    # sorted by filename to zip them together correctly later on!
    gold_files = [file for file in os.listdir(gold_dir) if file.endswith(".test.conll")]
    gold_files = sorted(gold_files, key=lambda x: (x.split("."))[0])
    print("Gold files: ", gold_files)
    pred_files = [file for file in os.listdir(pred_dir) if file.endswith(".test.conll.out")]
    pred_files = sorted(pred_files, key=lambda x: (x.split("."))[0])
    print("Pred files: ", pred_files)


    # initializing result dicts:
    baseline_langs = ['en', 'de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja']
    data_baseline = {
        'Language': [],
        'slots': [],
        'intents': [],
        'fully correct': []
    }
    dialect_langs = ['en', 'de-st', 'de', 'gsw', 'de-ba', 'de-by']
    data_dialects = {
        'Language': [],
        'slots': [],
        'intents': [],
        'fully correct': []
    }

    all_langs = ['ar', 'da', 'de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw', 'id', 'it', 'ja', 'kk', 'lt', 'nap', 'nl', 'sr', 'tr', 'zh']
    data_all_langs = {
        'Language': [],
        'slots': [],
        'intents': [],
        'fully correct': []
    }


    for gold_file, pred_file in zip(gold_files, pred_files):
        gold_path = os.path.join(gold_dir, gold_file)
        pred_path = os.path.join(pred_dir, pred_file)

        goldSlots, goldIntents = readNlu(gold_path)
        predSlots, predIntents = readNlu(pred_path)

        name = gold_file.split(".")[0]
        print("Predicting on: ", name)

        # initialize this language to results dicts if part of them
        save_baseline = False
        save_dialects = False
        save_all = False

        if str(name) in baseline_langs:
            save_baseline = True
            data_baseline['Language'].append(name)

        if name in dialect_langs:
            save_dialects = True
            data_dialects['Language'].append(name)

        if name in all_langs:
            save_all = True
            data_all_langs['Language'].append(name)
    
        tp_st = 0
        fp_st = 0
        fn_st = 0
        fullyCor = 0
        corIntents = 0

        tp_lo_rec = 0
        fn_lo_rc = 0
        tp_lo_pre = 0
        fp_lo_pre = 0

        tp_ul = 0
        fp_ul = 0
        fn_ul = 0


        for goldSlot, goldIntent, predSlot, predIntent in zip(goldSlots, goldIntents, predSlots, predIntents):
            # intents
            if goldIntent == predIntent:
                corIntents += 1

            # slots
            goldSpans = toSpans(goldSlot)
            print("goldSpans", goldSpans)
            predSpans = toSpans(predSlot)
            print("predSpans", predSpans)

            overlap_st = len(goldSpans.intersection(predSpans))
            tp_st += overlap_st
            fp_st += len(predSpans) - overlap_st
            fn_st += len(goldSpans) - overlap_st

            overlap_ul = getUnlabeled(goldSpans, predSpans)
            tp_ul += overlap_ul
            fp_ul += len(predSpans) - overlap_ul
            fn_ul += len(goldSpans) - overlap_ul

            overlap_lo = getLooseOverlap(goldSpans, predSpans)
            tp_lo_rec += overlap_lo
            fn_lo_rc += len(goldSpans) - overlap_lo

            overlap_lo = getLooseOverlap(predSpans, goldSpans)
            tp_lo_pre += overlap_lo
            fp_lo_pre += len(predSpans) - overlap_lo

            # fully correct sentences
            if overlap_st == len(goldSpans) and len(goldSpans) == len(predSpans) and goldIntent == predIntent:
                fullyCor += 1


        # some info on the intents:
        # print("Intents: ", set(goldIntents))
        # print("Number of Intents: ", len(set(goldIntents)))

        print("Intents:")
        print(f"intent accuracy:\t{corIntents / len(goldSlots)}")
        intent_accurracy = round((corIntents / len(goldSlots) * 100.0), 1)

        if save_baseline:
            data_baseline['intents'].append(intent_accurracy)
            data_baseline['fully correct'].append(round(fullyCor/len(goldSlots) * 100.0, 1))
        if save_dialects:
            data_dialects['intents'].append(intent_accurracy)
            data_dialects['fully correct'].append(round(fullyCor/len(goldSlots) * 100.0, 1))
        if save_all:
            data_all_langs['intents'].append(intent_accurracy)
            data_all_langs['fully correct'].append(round(fullyCor/len(goldSlots) * 100.0, 1))

        print(f"\nfully correct examples: {round(fullyCor/len(goldSlots) * 100.0, 1)}\n")

        # tests on slots
        print("Slots:")
        # strict span f1 - both span and label must match exactly!
        prec = 0.0 if tp_st+fp_st == 0 else tp_st/(tp_st+fp_st)
        rec = 0.0 if tp_st+fn_st == 0 else tp_st/(tp_st+fn_st)
        print(f"strict recall:\t\t{rec:.3f}")
        print(f"strict precision:\t{prec:.3f}")
        f1 = 0.0 if prec+rec == 0.0 else 2 * (prec * rec) / (prec + rec)
        print(f"strict slot-f1:\t\t{f1:.3f}\n")
        f1 = round((f1 * 100.0), 1)

        if save_baseline:
            data_baseline['slots'].append(f1)
        if save_dialects:
            data_dialects['slots'].append(f1)
        if save_all:
            data_all_langs['slots'].append(f1)

        save_baseline = False
        save_dialects = False
        save_all = False

        tp = tp_ul
        fp = fp_ul
        fn = fn_ul

        # unlabeled - label-agnostic matching? - ignoring slot labels
        prec = 0.0 if tp+fp == 0 else tp/(tp+fp)
        rec = 0.0 if tp+fn == 0 else tp/(tp+fn)
        print(f"unlabeled recall:\t{rec:.3f}")
        print(f"unlabeled precision:\t{prec:.3f}")
        f1 = 0.0 if prec+rec == 0.0 else 2 * (prec * rec) / (prec + rec)
        print(f"unlabeled slot-f1:\t{f1:.3f}\n")

        # loose - partial overlap with same label
        prec = 0.0 if tp_lo_pre + fp_lo_pre == 0 else tp_lo_pre/(tp_lo_pre+fp_lo_pre)
        rec = 0.0 if tp_lo_rec+fn_lo_rc == 0 else tp_lo_rec/(tp_lo_rec+fn_lo_rc)
        print(f"loose recall:\t\t{rec:.3f}")
        print(f"loose precision:\t{prec:.3f}")
        f1 = 0.0 if prec+rec == 0.0 else 2 * (prec * rec) / (prec + rec)
        print(f"loose slot-f1:\t\t{f1:.3f}\n")

    if data_baseline['Language'] == baseline_langs:
        print("Baseline results:\n", data_baseline)
    if data_dialects['Language'] == dialect_langs:
        print("Dialects results:\n", data_dialects)
    if data_all_langs['Language'] == all_langs:
        print("All results:\n", data_all_langs)

    writeResults(data_all_langs, data_baseline, data_dialects, experiment_name)

