#!/bin/bash
# script to prepare evaluation data for all languages in Colab (gets removed when quitting runtime of notebook)

mkdir -p /content/BaySIDshot/alllangs_eval_data/

cp /content/BaySIDshot/de-by.test.conll /content/BaySIDshot/alllangs_eval_data/
cp /content/BaySIDshot/de-by.valid.conll /content/BaySIDshot/alllangs_eval_data/

cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.test.conll /content/BaySIDshot/alllangs_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.5/de-ba.valid.conll /content/BaySIDshot/alllangs_eval_data/
python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py /content/BaySIDshot/alllangs_eval_data/de-ba.test.conll
python3 /content/BaySIDshot/scripts/reorganize_miriams_data.py /content/BaySIDshot/alllangs_eval_data/de-ba.valid.conll

cp /content/BaySIDshot/xsid/data/xSID-0.5/*.test.conll /content/BaySIDshot/alllangs_eval_data/
cp /content/BaySIDshot/xsid/data/xSID-0.5/*.valid.conll /content/BaySIDshot/alllangs_eval_data/
