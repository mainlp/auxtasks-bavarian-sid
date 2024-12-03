## BaySIDshot

This repository contains both code and submodules used for my Master's Thesis entitled _Analyzing Slot and Intent Detection for Upper German Dialects via Zero-Shot Transfer Learning_ as well as for our related paper [_Improving Dialectal Slot and Intent Detection with Auxiliary Tasks: A Multi-Dialectal Bavarian Case Study_](https://sites.google.com/view/vardial-2025) which builds upon the thesis and was co-authored by Verena Blaschke and Prof. Barbara Plank .

The origin of the portmanteau *BaySIDshot* is rooted in the creation of a new additional Bavarian test and validation set depicting the dialect spoken in the Munich region in order to further analyze zero-shot transfer learning performance on slot and intent detection (SID) for this and other Upper German dialects.
Both _de-by_ (_de-muc_ in the paper!) test and validation .conll files can be found at the root of this directory and featured in the latest version of [xSID](https://github.com/mainlp/xsid).
Thus, this work presents a parallel extension to the Upper Bavarian dataset translated and annotated by [Winkler et al. (2024)](https://aclanthology.org/2024.lrec-main.1297/), similarly building on and extending the xSID approach and data format initiated by [van der Goot et al. (2021b)](https://aclanthology.org/2021.naacl-main.197/). 
For running the baseline and extended experiments, recursively cloning all submodules and especially [_MaChAmp_](https://github.com/machamp-nlp/machamp) by [van der Goot et al. (2021a)](https://aclanthology.org/2021.eacl-demos.22/) is necessary and can be done by using the following command:
```
git clone https://github.com/XaverKrueckl/BaySIDshot.git --recurse-submodules
```
As a main approach to analyze and enhance zero-shot SID transfer learning to Upper German dialects, auxiliary task training is performed on four different task types from three Bavarian target language datasets.
In concrete, these are a [Bavarian Universal Dependencies (UD) set](https://github.com/UniversalDependencies/UD_Bavarian-MaiBaam) by [Blaschke et al. (2024)](https://aclanthology.org/2024.lrec-main.953/), a [Bavarian Named Entity Recognition (NER) set](https://github.com/mainlp/BarNER/tree/main/data/BarNER-final) by [Peng et al. (2024)](https://aclanthology.org/2024.lrec-main.1262/) and [Masked-Language-Modeling (MLM) data](https://github.com/mainlp/dialect-BLI/blob/main/labelled_data/bitext/bar/ann_1.csv) taken as preprocessed sentences from [Artemova and Plank (2023)](https://aclanthology.org/2023.nodalida-1.39/).
Whilst both UD and MLM the data consists of one overall set, the NER data is split into two subsets, referred to according to their source as Wiki and Twitter. In the experiments below, both are [automatically merged into one dataset](https://github.com/machamp-nlp/machamp/tree/master?tab=readme-ov-file#training-on-multiple-datasets) by _MaChAmp_ as they feature the same task type in the configuration files. It has to be mentioned, that the Twitter data is only available for scientific research by contacting the authors. 
Please always cite the respective data source if used in your work!

In order to recreate both baseline and extended experiment results, running the respective notebooks in Google Colaboratory is required.
To do so, getting a Pro subscription on the cloud-based service is recommended for the baseline and required for the extended experiments for which larger and stable GPU ressoures are necessary.
Similarly, a Google account with access to Google Drive is suggested in order to save models and outputs out of the runtime environment.

Starting the notebooks will establish a mount on Google Drive and then clones this repository recursively.
If required, data preparation scripts from the respecitve [scripts](https://github.com/XaverKrueckl/BaySIDshot/tree/main/scripts) directory are run.
The created datasets, for which the paths are set accordingly in the [configurations](https://github.com/XaverKrueckl/BaySIDshot/tree/main/configs) for _MaChAmp_ are only present during runtime.
If their creation fails, the openly available data is given in a [manual data](https://github.com/XaverKrueckl/BaySIDshot/tree/main/manual_data) directory.
In order to use this data, it has to be pre-processed and the paths to the data in the [configuration files](https://github.com/XaverKrueckl/BaySIDshot/tree/main/configs) need to be adjusted to this directory.

After installing the required modules for _MaChAmp_, the notebook then checks for GPU access and general operability.
For each experiment, the respective [configuration and parameter files](https://github.com/XaverKrueckl/BaySIDshot/tree/main/configs) are inspected before the train command is started.
After the fine-tuning process has finished, each resulting model in the log files is saved to Google Drive, carrying the experiment name.
Before the prediction on the final model starts, the respecitve evaluation data is prepared via [scripts](https://github.com/XaverKrueckl/BaySIDshot/tree/main/scripts) but also available as gold files in the [manual data](https://github.com/XaverKrueckl/BaySIDshot/tree/main/manual_data).
In a rather complex evaluation cell, a script is being prepared that evaluates the final model, which only needs to be loaded once, on each evaluation file from the prepared set. 
The predicted output files are saved to the respective model on Google Drive.
Similarly, a separate evaluation [script](https://github.com/XaverKrueckl/BaySIDshot/tree/main/scripts) is run to get the results in a clear json file containing three objects depending on the extent of the evaluation set.
After having run an experiment on multiple random seed, further [scripts](https://github.com/XaverKrueckl/BaySIDshot/tree/main/scripts) can be used to get the average over these runs, to turn this into a .csv document for usage in a LaTex tables generator and to produce confusion matrices on the results of intent classification.
In their current state, the notebooks run all experiments on random_seed=1234. 
The two further seeds that were used are 6543 and 8446. These need to be set for each experiment and in the respective model names!

Finally, please find the Tex and Bib files as well as styleguide, figures and the final thesis pdf produced using Overleaf [here](https://github.com/XaverKrueckl/BaySIDshot/tree/main/thesis).

When using this work or data utilized in it, please cite the respective papers!
For questions and access to unpublished NER data, please contact me!

Cheers,
Xaver
