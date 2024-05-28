#!/usr/bin/python3

import pandas as pd

# dialects data!

def average_scores(data1, data2, data3):
    # Ensure the languages are the same in all data inputs
    if data1['Language'] != data2['Language'] or data2['Language'] != data3['Language']:
        raise ValueError("Languages in input data do not match.")

    languages = data1['Language']
    avg_slots = []
    avg_intents = []

    for i in range(len(languages)):
        avg_slot = round((data1['slots'][i] + data2['slots'][i] + data3['slots'][i]) / 3, 1)
        avg_intent = round((data1['intents'][i] + data2['intents'][i] + data3['intents'][i]) / 3, 1)
        avg_slots.append(avg_slot)
        avg_intents.append(avg_intent)

    return {
        'Language': languages,
        'slots': avg_slots,
        'intents': avg_intents
    }

data_mBERT = {
    'Language': ['en', 'de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja'],
    'slots': [97.6, 48.5, 33.0, 73.9, 80.4, 75.0, 67.4, 71.1, 45.8, 72.9, 48.5, 55.7, 59.9],
    'intents': [99.7, 67.8, 74.2, 87.5, 72.3, 81.7, 75.7, 80.7, 63.1, 83.3, 60.1, 74.7, 53.9]
}

data_XLM15 = {
    'Language': ['en', 'de-st', 'de', 'da', 'nl', 'it', 'sr', 'id', 'ar', 'zh', 'kk', 'tr', 'ja'],
    'slots': [97.0, 39.4, 33.3, 26.3, 30.9, 27.3, 15.9, 14.9, 49.1, 57.6, 10.9, 45.5, 33.4],
    'intents': [99.7, 61.3, 78.5, 56.3, 45.4, 48.0, 41.4, 36.4, 67.5, 78.8, 29.9, 67.3, 39.1]
}

# my data
# mBERT base

data_mBERT_1234 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [67.2, 44.9, 45.6, 40.1, 94.4, 22.2], 'intents': [73.8, 65.4, 59.6, 65.6, 99.0, 51.8]}

data_mBERT_6543 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [67.8, 42.4, 43.7, 41.1, 93.7, 19.4], 'intents': [73.4, 63.0, 62.4, 63.4, 99.2, 47.0]}

data_mBERT_8446 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [70.1, 42.5, 43.0, 42.6, 94.1, 22.3], 'intents': [77.2, 68.8, 62.0, 68.4, 98.8, 47.4]}

average_mBERT = average_scores(data_mBERT_1234, data_mBERT_8446, data_mBERT_8446)


# XLMR base

data_XLMR_1234 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [75.4, 36.5, 33.9, 32.8, 93.2, 13.9], 'intents': [90.8, 69.8, 56.0, 72.0, 98.8, 44.4]}

data_XLMR_6543 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [72.3, 35.2, 36.5, 31.1, 94.0, 13.7], 'intents': [89.4, 68.4, 58.4, 69.2, 99.0, 50.6]}

data_XLMR_8446 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [73.5, 34.8, 32.8, 32.5, 94.3, 15.0], 'intents': [86.6, 68.4, 52.0, 71.4, 99.2, 46.2]}

average_XLMR = average_scores(data_XLMR_1234, data_XLMR_6543, data_XLMR_8446)


# mDeBERTa base

data_mDeBERTa_1234 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [84.0, 45.4, 42.1, 45.3, 95.4, 18.4], 'intents': [97.8, 77.8, 60.6, 78.6, 99.2, 54.0]}

data_mDeBERTa_6543 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [83.0, 49.6, 43.5, 47.4, 95.0, 24.1], 'intents': [98.4, 78.6, 65.0, 79.0, 99.2, 58.0]}

data_mDeBERTa_8446 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [82.3, 45.3, 44.4, 45.3, 95.0, 19.5], 'intents': [97.4, 76.8, 68.2, 77.2, 99.0, 60.6]}

average_mDeBERTa = average_scores(data_mDeBERTa_1234, data_mBERT_6543, data_mDeBERTa_8446)

# gBERT base

data_gBERT_1234 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [79.3, 49.4, 48.8, 49.0, 93.2, 30.4], 'intents': [84.2, 68.8, 71.0, 73.2, 99.2, 66.0]}

data_gBERT_6543 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [77.7, 47.7, 45.7, 42.9, 94.1, 28.8], 'intents': [81.2, 69.8, 64.4, 73.0, 99.2, 63.4]}

data_gBERT_8446 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [79.4, 47.8, 46.7, 47.5, 93.8, 30.9], 'intents': [83.4, 68.8, 68.2, 75.2, 99.2, 62.4]}


average_gBERT = average_scores(data_gBERT_1234, data_gBERT_6543, data_gBERT_8446)

# first experiment - mDeBERTa first trained on UD EWT bavarian train english dev then NLU as before:

#data_exp21_8446 = {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [81.2, 56.0, 54.7, 52.0, 95.7, 24.6], 'intents': [88.4, 81.2, 70.6, 77.0, 99.4, 67.2]}
data_mDeBERTa_exp1_ewt_nlu_1234 =  {'Language': ['de', 'de-ba', 'de-by', 'de-st', 'en', 'gsw'], 'slots': [83.0, 50.8, 45.5, 45.5, 95.3, 22.7], 'intents': [95.4, 76.2, 58.8, 75.0, 99.4, 53.0]}



# Create multi-index DataFrame for mBERT
#df_mBERT = pd.DataFrame(data_mBERT)
#df_mBERT.set_index('Language', inplace=True)
#df_mBERT.columns = pd.MultiIndex.from_product([['mBERT-xSID'], df_mBERT.columns])

# Create multi-index DataFrame for XLM15
#df_XLM15 = pd.DataFrame(data_XLM15)
#df_XLM15.set_index('Language', inplace=True)
#df_XLM15.columns = pd.MultiIndex.from_product([['XLM15-xSID'], df_XLM15.columns])

# Create multi-index DataFrame for mBERT_me
df_mBERT = pd.DataFrame(average_mBERT)
df_mBERT.set_index('Language', inplace=True)
df_mBERT.columns = pd.MultiIndex.from_product([['mBERT'], df_mBERT.columns])

# Create multi-index DataFrame for XLMR_me
df_XLMR = pd.DataFrame(average_XLMR)
df_XLMR.set_index('Language', inplace=True)
df_XLMR.columns = pd.MultiIndex.from_product([['XLMR'], df_XLMR.columns])

# Create multi-index DataFrame for mDeBERTa
df_mDeBERTa = pd.DataFrame(average_mDeBERTa)
df_mDeBERTa.set_index('Language', inplace=True)
df_mDeBERTa.columns = pd.MultiIndex.from_product([['mDeBERTa'], df_mDeBERTa.columns])

# Create multi-index DataFrame for gBERT
df_gBERT = pd.DataFrame(average_gBERT)
df_gBERT.set_index('Language', inplace=True)
df_gBERT.columns = pd.MultiIndex.from_product([['gBERT'], df_gBERT.columns])

# Create multi-index DataFrame for mDeBERTa_exp1ewt
df_mDeBERTa_epx1ewt = pd.DataFrame(data_mDeBERTa_exp1_ewt_nlu_1234)
df_mDeBERTa_epx1ewt.set_index('Language', inplace=True)
df_mDeBERTa_epx1ewt.columns = pd.MultiIndex.from_product([['mDeBERTa-EXP1EWT'], df_mDeBERTa_epx1ewt.columns])



# Merge the DataFrames ensuring the correct language order - experiment not included for now!
df_concatenated = pd.concat([df_mBERT, df_XLMR, df_gBERT, df_mDeBERTa, df_mDeBERTa_epx1ewt], axis=1)




# Calculate the average values excluding "en" for each metric and each model
slots_avg_mBERT = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT', 'slots')].mean()
intents_avg_mBERT = df_concatenated.loc[df_concatenated.index != 'en', ('mBERT', 'intents')].mean()

slots_avg_XLMR = df_concatenated.loc[df_concatenated.index != 'en', ('XLMR', 'slots')].mean()
intents_avg_XLMR = df_concatenated.loc[df_concatenated.index != 'en', ('XLMR', 'intents')].mean()

slots_avg_mDeBERTa = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa', 'slots')].mean()
intents_avg_mDeBERTa  = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa', 'intents')].mean()

slots_avg_gBERT = df_concatenated.loc[df_concatenated.index != 'en', ('gBERT', 'slots')].mean()
intents_avg_gBERT = df_concatenated.loc[df_concatenated.index != 'en', ('gBERT', 'intents')].mean()

slots_avg_mDeBERTa_exp = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa-EXP1EWT', 'slots')].mean()
intents_avg_mDeBERTa_exp = df_concatenated.loc[df_concatenated.index != 'en', ('mDeBERTa-EXP1EWT', 'intents')].mean()

# Format the average values to have only one digit after the decimal point

slots_avg_mBERT_formatted = '{:.1f}'.format(slots_avg_mBERT)
intents_avg_mBERT_formatted = '{:.1f}'.format(intents_avg_mBERT)

slots_avg_XLMR_formatted = '{:.1f}'.format(slots_avg_XLMR)
intents_avg_XLMR_formatted = '{:.1f}'.format(intents_avg_XLMR)

slots_avg_mDeBERTa_formatted = '{:.1f}'.format(slots_avg_mDeBERTa)
intents_avg_mDeBERTa_formatted = '{:.1f}'.format(intents_avg_mDeBERTa)

slots_avg_gBERT_formatted = '{:.1f}'.format(slots_avg_gBERT)
intents_avg_gBERT_formatted = '{:.1f}'.format(intents_avg_gBERT)

slots_avg_mDeBERTa_exp1ewt_formatted = '{:.1f}'.format(slots_avg_mDeBERTa_exp)
intents_avg_mDeBERTa_exp1ewt_formatted = '{:.1f}'.format(intents_avg_mDeBERTa_exp)

# Create DataFrames containing the average values
avg_data = {
    ('mBERT', 'slots'): [slots_avg_mBERT_formatted],
    ('mBERT', 'intents'): [intents_avg_mBERT_formatted],
    ('XLMR', 'slots'): [slots_avg_XLMR_formatted],
    ('XLMR', 'intents'): [intents_avg_XLMR_formatted],
    ('gBERT', 'slots'): [slots_avg_gBERT_formatted],
    ('gBERT', 'intents'): [intents_avg_gBERT_formatted],
    ('mDeBERTa', 'slots'): [slots_avg_mDeBERTa_formatted],
    ('mDeBERTa', 'intents'): [intents_avg_mDeBERTa_formatted],
    ('mDeBERTa-EXP1EWT', 'slots'): [slots_avg_mDeBERTa_exp1ewt_formatted],
    ('mDeBERTa-EXP1EWT', 'intents'): [intents_avg_mDeBERTa_exp1ewt_formatted]
}


df_avg = pd.DataFrame(avg_data, index=['Avg.'])

# Concatenate the average DataFrame with df_concatenated
df_concatenated_with_avg = pd.concat([df_concatenated, df_avg])

print(df_concatenated_with_avg)
