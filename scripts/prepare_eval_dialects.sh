#!/bin/bash
mkdir -p dialects_eval_data
cd dialects_eval_data

# copy dialects eval data together:

cp /content/BaySIDshot/de-by.test.conll .
cp /content/BaySIDshot/de-by.dev.conll .

cp /content/BaySIDshot/xsid/ .