import numpy as np
import nltk


def stats(filename):
    print(filename)
    sentence_lengths = []
    word_lengths = []
    slot_lengths = []
    n_split_slots = 0
    sent_id2slot2words = {}
    sent_id2slot_order = {}
    sent_id2text = {}
    sent_id = 0
    slots_total = 0
    with open(filename) as f:
        sent_len = 0
        slot_len = 0
        slots_in_sent = []
        for line in f:
            line = line.strip()
            if not line:
                if sent_len > 0:
                    sentence_lengths.append(sent_len)
                sent_len = 0
                if slot_len > 0:
                    slot_lengths.append(slot_len)
                slot_len = 0
                if sent_id not in sent_id2slot2words:
                    sent_id2slot2words[sent_id] = {}
                else:
                    slots_total += len(sent_id2slot2words[sent_id])
                sent_id2slot_order[sent_id] = slots_in_sent
                slots_in_sent = []
                continue
            if line[0] == "#":
                if line.startswith("# text:"):
                    sent_id += 1
                    sent_id2text[sent_id] = line[11:]
                continue
            sent_len += 1
            _, word, _, slot = line.split()
            word_lengths.append(len(word))
            if slot == "O":
                if slot_len > 0:
                    slot_lengths.append(slot_len)
                slot_len = 0
            else:
                if slot[0] == "B":
                    if slot_len > 0:
                        slot_lengths.append(slot_len)
                    slot_len = 1
                    if slot in slots_in_sent:
                        n_split_slots += 1
                    slots_in_sent.append(slot)
                else:  # I
                    slot_len += 1
                slot_type = slot[2:]
                try:
                    sent_id2slot2words[sent_id][slot_type].append(word)
                except KeyError:
                    try:
                        sent_id2slot2words[sent_id][slot_type] = [word]
                    except KeyError:
                        sent_id2slot2words[sent_id] = {slot_type: [word]}

    print("avg sentence length", np.mean(sentence_lengths), np.std(sentence_lengths))
    print("avg word length", np.mean(word_lengths))
    print("avg slot length", np.mean(slot_lengths))
    print("split slot freq", n_split_slots / slots_total)
    print()
    return sent_id2slot2words, sent_id2slot_order, sent_id2text


def pair_stats(lang1, lang2, lang2sent_id2slot2words, lang2sent_id2slot_order, lang2sent_id2text):
    distances = []
    distances_lower = []
    distances_sent = []
    distances_sent_lower = []
    slot_diffs = 0
    slot_order_diffs = 0
    for sent_id in lang2sent_id2slot2words[lang1]:
        slot_order1 = lang2sent_id2slot_order[lang1][sent_id]
        slot_order2 = lang2sent_id2slot_order[lang2][sent_id]
        if slot_order1 != slot_order2:
            slot_order_diffs += 1
        sent1 = lang2sent_id2text[lang1][sent_id]
        sent2 = lang2sent_id2text[lang2][sent_id]
        max_len = len(sent1.split())
        if len(sent2.split()) > max_len:
            max_len = len(sent2.split())
        distances_sent.append(nltk.edit_distance(sent1.split(), sent2.split()) / max_len)
        distances_sent_lower.append(nltk.edit_distance(sent1.lower().split(), sent2.lower().split()) / max_len)
        for slot in lang2sent_id2slot2words[lang1][sent_id]:
            try:
                entry1 = " ".join(lang2sent_id2slot2words[lang1][sent_id][slot])
                entry2 = " ".join(lang2sent_id2slot2words[lang2][sent_id][slot])
            except KeyError:
                slot_diffs += 1
                continue
            dist = nltk.edit_distance(entry1, entry2)
            dist_lower = nltk.edit_distance(entry1.lower(), entry2.lower())
            max_len = len(entry1)
            if len(entry2) > max_len:
                max_len = len(entry2)
            distances.append(dist / max_len)
            distances_lower.append(dist_lower / max_len)
        try:
            for slot in lang2sent_id2slot2words[lang2][sent_id]:
                if slot not in lang2sent_id2slot2words[lang1][sent_id]:
                    slot_diffs += 1
        except KeyError:
            print(lang2, sent_id)
            print(lang2sent_id2slot2words[lang2])

    print(lang1, lang2)
    print("mean sim", 1 - np.mean(distances))
    print("mean sim (lower)", 1 - np.mean(distances_lower))
    print("mean sim (sent)", 1 - np.mean(distances_sent))
    print("mean sim (sent, lower)", 1 - np.mean(distances_sent_lower))
    print("slot_diffs", slot_diffs)
    print("slot_order_diffs", slot_order_diffs / len(lang2sent_id2slot2words[lang1]))


for i in range(len(langs) - 1):
    for j in range(len(langs) - 1 - i):
        pair_stats(langs[i], langs[i + j + 1], lang2sent_id2slot2words, lang2sent_id2slot_order, lang2sent_id2text)
