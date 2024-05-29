#!/bin/bash
mkdir -p baseline_eval_data
cd baseline_eval_data

# copy baseline eval data together:
# adapt absolute paths for out of colab cases!

cp /content/BaySIDshot/xsid/data/xSID/*.test.conll .
cp /content/BaySIDshot/xsid/data/xSID/*.valid.conll .

cd ..