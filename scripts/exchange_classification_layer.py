#!/usr/bin/python3

import sys
import torch

def load_model(filepath):
    return torch.load(filepath, map_location=torch.device('cuda'))

def replace_classification_layer(model0_path, model1_path, model_out_path):
    # Load the first model and extract its classification layer
    model0 = load_model(model0_path)
    classification_layer = model0.classifier

    # Load the second model
    model1 = load_model(model1_path)

    # Set the classification layer of the first model as the classification layer in the second model
    model1.classifier = classification_layer

    # Save the modified second model
    torch.save(model1, model_out_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 exchange_classification_layer.py <model0_path> <model1_path> <model_out_path>")
        sys.exit(1)

    replace_classification_layer(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Successfully replaced the classification layer and saved the modified second model.")

# Extracting a model after finetuning
# If you would like to re-use your MaChAmp finetuned model in another toolkit, you can extract the
# `transformers` model. We provide an example script in `scripts/misc/extract_automodel.py`, which
# needs to be ran from the root of this repo. Usage is as follows:

# cp scripts/misc/extract_automodel.py .
# python3 extract_automodel.py logs/ewt/*/model.pt mBERT_finetuned_on_EWT
#
# Now the models including its configuration and tokenizer will be written in a folder titled
# `mBERT_finetuned_on_EWT`.
