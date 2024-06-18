#!/usr/bin/python3

import sys
import torch
import torch.nn as nn
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoModel


class CombinedModel(nn.Module):
    def __init__(self, encoder, decoder1, decoder2):
        super(CombinedModel, self).__init__()
        self.encoder = encoder
        self.decoder1 = decoder1
        self.decoder2 = decoder2

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        encoder_outputs = self.encoder(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)

        # Assuming the encoder output is the last hidden state
        sequence_output = encoder_outputs.last_hidden_state

        # Apply both decoders to the encoder output
        task1_output = self.decoder1(sequence_output)
        task2_output = self.decoder2(sequence_output)

        return task1_output, task2_output


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python3 exchange_classification_layer.py <model0_dir> <model1_dir> <model_out_dir>")
        sys.exit(1)

    model0_dir = sys.argv[1]
    model1_dir = sys.argv[2]
    model_out_dir = sys.argv[3]

    # Load the first model and extract its decoders
    model0 = AutoModelForSequenceClassification.from_pretrained(model0_dir)

    # Assuming model0 has two decoders, extract them
    decoder1_model0 = model0.classifier1  # Modify this based on your actual model architecture
    decoder2_model0 = model0.classifier2  # Modify this based on your actual model architecture

    # Load the second model
    model1 = AutoModel.from_pretrained(model1_dir)

    # Create a new combined model
    combined_model = CombinedModel(encoder=model1, decoder1=decoder1_model0, decoder2=decoder2_model0)

    # Save the modified combined model
    combined_model_save_path = model_out_dir + "/pytorch_model.bin"
    torch.save(combined_model.state_dict(), combined_model_save_path)

    # Also save the tokenizer if needed
    tokenizer = AutoTokenizer.from_pretrained(model0_dir)
    tokenizer.save_pretrained(model_out_dir)

    print(
        "Successfully combined the encoder from the second model with the decoders from the first model and saved the modified model.")
