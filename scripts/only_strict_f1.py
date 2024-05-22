#!/usr/bin/python3

import sys

from typing import List, Tuple, Set


def readNlu(path: str) -> Tuple[ List[List[str]], List[str]]:
    slots = []
    intents = []
    curSlots = []
    for line in open(path):
        line = line.strip()
        if line.startswith('# intent: '):
            intents.append(line[10:].strip())
        if line == '':
            slots.append(curSlots)
            curSlots = []
        elif line[0] == '#' and len(line.split('\t')) == 1:
            continue
        else:
            curSlots.append(line.split('\t')[-1])
            
    return slots, intents


def toSpans(tags: List[str]) -> Set[str]:
    spans = set()
    for beg in range(len(tags)):
        if tags[beg][0] == 'B':
            end = beg
            for end in range(beg+1, len(tags)):
                if tags[end][0] != 'I':
                    break
            spans.add(str(beg) + '-' + str(end) + ':' + tags[beg][2:])
            
    return spans

    
    


if __name__ == '__main__':
    # give gold file as first and pred file as second command line argument
    goldSlots, goldIntents = readNlu(sys.argv[1])
    predSlots, predIntents = readNlu(sys.argv[2])

    tp = 0
    fp = 0
    fn = 0

    for goldSlot, predSlot in zip(goldSlots, predSlots):
        goldSpans = toSpans(goldSlot)
        predSpans = toSpans(predSlot)
        print("goldSlot:", goldSlot)
        print("predSlot:", predSlot)
        print("goldSpan:", goldSpans)
        print("predSpan:", predSpans)

        correct = len(goldSpans.intersection(predSpans))
        print("correct: ", correct)
        incorrect = len(goldSpans) - correct if len(goldSpans) == len(predSpans) else 0
        print("incorrect: ", incorrect)
        tp += correct
        print("tp: ", tp)
        fp += len(predSpans) - correct
        print("fp: ", fp)
        fn += len(goldSpans) - correct
        print("fn: ", fn)
        print()

    prec = 0.0 if tp + fp == 0 else tp / (tp + fp)
    rec = 0.0 if tp + fn == 0 else tp / (tp + fn)
    f1 = 0.0 if prec + rec == 0.0 else 2 * (prec * rec) / (prec + rec)

    print(f"strict recall:\t\t{rec:.3f}")
    print(f"strict precision:\t{prec:.3f}")
    print(f"strict slot-f1:\t\t{f1:.3f}")