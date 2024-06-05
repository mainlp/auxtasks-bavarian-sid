#!/bin/bash
# script to prepare baseline evaluation data in Colab, (gets removed when quitting runtime of notebook)

mkdir -p /content/BaySIDshot/baseline_eval_data

cp /content/BaySIDshot/xsid/data/xSID/*.test.conll /content/BaySIDshot/baseline_eval_data/
cp /content/BaySIDshot/xsid/data/xSID/*.valid.conll /content/BaySIDshot/baseline_eval_data/
