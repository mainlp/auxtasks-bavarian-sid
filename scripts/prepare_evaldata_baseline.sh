#!/bin/bash
# script to prepare baseline evaluation data
mkdir -p /content/BaySIDshot/baseline_eval_data

# copy baseline eval data together, paths according to usage in Colab:

cp /content/BaySIDshot/xsid/data/xSID/*.test.conll /content/BaySIDshot/baseline_eval_data/
cp /content/BaySIDshot/xsid/data/xSID/*.valid.conll /content/BaySIDshot/baseline_eval_data/
