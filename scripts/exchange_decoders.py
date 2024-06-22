#!/usr/bin/python3

import sys
import torch
import torch.nn as nn
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModel


# Define a custom model to combine encoder and multiple decoders
class CombinedModel(nn.Module):
    def __init__(self, encoder, classifier):
        super(CombinedModel, self).__init__()
        self.encoder = encoder
        self.classifier = classifier

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        encoder_outputs = self.encoder(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)

        # Assuming the encoder output is the last hidden state
        sequence_output = encoder_outputs.last_hidden_state

        # Apply the classifier to the encoder output
        classification_output = self.classifier(
            sequence_output[:, 0, :])  # Assuming we're using the [CLS] token's output

        return classification_output


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 exchange_decoders.py <model0_dir> <model1_dir> <model_out_dir>")
        sys.exit(1)

    model0_dir = sys.argv[1]
    model1_dir = sys.argv[2]
    model_out_dir = sys.argv[3]

    # Load the first model and inspect its architecture to find the decoder layers
    model0 = AutoModelForSequenceClassification.from_pretrained(model0_dir, config=model0_dir + "config.json")
    print("Model 0 Architecture:")
    print(model0)

    # Extract the classifier layer
    classifier_model0 = model0.classifier

    # Load the second model (just the encoder)
    model1 = AutoModel.from_pretrained(model1_dir)
    print("Model 1 Architecture:")
    print(model1)

    # Create a new combined model
    combined_model = CombinedModel(encoder=model1, classifier=classifier_model0)

    # Save the modified combined model
    combined_model_save_path = model_out_dir + "/pytorch_model.bin"
    torch.save(combined_model.state_dict(), combined_model_save_path)

    # Also save the tokenizer if needed
    tokenizer = AutoTokenizer.from_pretrained(model0_dir)
    tokenizer.save_pretrained(model_out_dir)

    model0.config.save_pretrained(model_out_dir)

    print(
        "Successfully combined the encoder from the second model with the classifier from the first model and saved the modified model.")

# Todo: gives back a corrupted state dict