# Improving Dialectal Slot and Intent Detection with Auxiliary Tasks: A Multi-Dialectal Bavarian Case Study

## Introduction

This repository contains the code for the paper _Improving Dialectal Slot and Intent Detection with Auxiliary Tasks: A Multi-Dialectal Bavarian Case Study_ (Xaver Maria Krückl*, Verena Blaschke*, Barbara Plank; VarDial 2025).

### Abstract

Reliable slot and intent detection (SID) is crucial in natural language understanding for applications like digital assistants. Encoder-only transformer models fine-tuned on high-resource languages generally perform well on SID. However, they struggle with dialectal data, where no standardized form exists and training data is scarce and costly to produce. We explore zero-shot transfer learning for SID, focusing on multiple Bavarian dialects, for which we release a new dataset for the Munich dialect. We evaluate models trained on auxiliary tasks in Bavarian, and compare joint multi-task learning with intermediate-task training. We also compare three types of auxiliary tasks: token-level syntactic tasks, named entity recognition (NER), and language modelling. We find that the included auxiliary tasks have a more positive effect on slot filling than intent classification (with NER having the most positive effect), and that intermediate-task training yields more consistent performance gains. Our best-performing approach improves intent classification performance on Bavarian dialects by 5.1 and slot filling F1 by 8.4 percentage points.

### Citation

If you use this code, please cite:

```
@inproceedings{krueckl-etal-2025-improving,
  title={Improving Dialectal Slot and Intent Detection with Auxiliary Tasks: {A} Multi-Dialectal {Bavarian} Case Study},
  author={Krückl, Xaver Maria and Blaschke, Verena and Plank, Barbara},
  year={2025},
  booktitle={Proceedings of the Twelfth Workshop on NLP for Similar Languages, Varieties and Dialects (VarDial)},
  editor = {Scherrer, Yves and Jauhiainen, Tommi and Ljube{\v{s}}i{\'c}, Nikola and Zampieri, Marcos and Nakov, Preslav and Tiedemann, J{\"o}rg},
  booktitle = "Proceedings of the Twelfth Workshop on NLP for Similar Languages, Varieties, and Dialects (VarDial 2025)",
  month = jan,
  year = 2025,
  address = "Abu Dhabi, UAE",
  publisher = "International Committee on Computational Linguistics",
}
```

## Data

### Munich Bavarian xSID
The new Munich Bavarian development and test sets will be included in an official [xSID](https://github.com/mainlp/xsid) release. You can already find them in the root of this repository.

**NOTE:** In the paper (and the official xSID release), the new dataset is called *de-muc*. In the subforlders and scripts of this repository, it is called *de-by*.

### Other datasets

- The [xSID](https://github.com/mainlp/xsid) datasets are shared under the [CC BY-SA 4.0](https://github.com/mainlp/xsid/blob/main/LICENSE) license.
- The [UD MaiBaam](https://github.com/UniversalDependencies/UD_Bavarian-MaiBaam) dataset is also shared under the [CC BY-SA 4.0](https://github.com/UniversalDependencies/UD_Bavarian-MaiBaam/blob/master/LICENSE.txt) license.
- We use Bavarian Wikipedia data ([CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en)) for NER ([BarNER](https://github.com/mainlp/BarNER/)) and MLM ([dialect-BLI](https://github.com/mainlp/dialect-BLI)). For the remaining part of BarNER, please reach out to the authors of the respective [dataset paper](https://aclanthology.org/2024.lrec-main.1262/).
- We also use the MAS:de-ba and nat:de-ba datasets from [NaLiBaSID](https://github.com/mainlp/NaLiBaSID).

## Code + usage

For running the baseline and extended experiments, recursively cloning all submodules and especially [_MaChAmp_](https://github.com/machamp-nlp/machamp) by [van der Goot et al. (2021a)](https://aclanthology.org/2021.eacl-demos.22/) is necessary and can be done by using the following command:
```
git clone https://github.com/mainlp/auxtasks-bavarian-sid.git --recurse-submodules
```

The code in `notebooks` was originally run on Google Colaboratory; you will need to update some paths to make the code work outside of Google Colab and/or with your Google Drive set-up.

Starting the notebooks will establish a mount on Google Drive and then clones this repository recursively.

If required, data preparation scripts from the respective [scripts](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/scripts) directory are run.
The created datasets, for which the paths are set accordingly in the [configurations](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/configs) for _MaChAmp_ are only present during runtime.
If their creation fails, the openly available data is given in a [manual data](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/manual_data) directory.
In order to use this data, it has to be pre-processed and the paths to the data in the [configuration files](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/configs) need to be adjusted to this directory. 

After installing the required modules for _MaChAmp_, the notebook then checks for GPU access and general operability.
For each experiment, the respective [configuration and parameter files](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/configs) are inspected before the train command is started.

Whilst both UD and MLM the data consists of one overall set, the NER data is split into two subsets, referred to according to their source as Wiki and Twitter. In the experiments below, both are [automatically merged into one dataset](https://github.com/machamp-nlp/machamp/tree/master?tab=readme-ov-file#training-on-multiple-datasets) by _MaChAmp_ as they feature the same task type in the configuration files.

After the fine-tuning process has finished, each resulting model in the log files is saved to Google Drive, carrying the experiment name.
Before the prediction on the final model starts, the respecitve evaluation data is prepared via [scripts](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/scripts) but also available as gold files in the [manual data](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/manual_data).

In the evaluation cell, a script evaluates the final model, which only needs to be loaded once, on each evaluation file from the prepared set. 
The predicted output files are saved to the respective model on Google Drive.
Similarly, a separate evaluation [script](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/scripts) is run to get the results in a clear json file containing three objects depending on the extent of the evaluation set.

After having run an experiment on multiple random seed, further [scripts](https://github.com/mainlp/auxtasks-bavarian-sid/tree/main/scripts) can be used to get the average over these runs, to turn this into a .csv document for usage in a LaTex tables generator and to produce confusion matrices on the results of intent classification.

In their current state, the notebooks run all experiments on random_seed=1234. 
The two further seeds that were used are 6543 and 8446. These need to be set for each experiment and in the respective model names!
