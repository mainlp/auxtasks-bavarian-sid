import os
import torch
from collections import Counter
from transformers import AutoModelForTokenClassification, AutoTokenizer

# Define your intents and slots (as defined in your original code)
# add this unknown class?
intents = [
    "@@unkORpad@@", "weather / find", "alarm / set_alarm", "alarm / show_alarms",
    "reminder / set_reminder", "alarm / modify_alarm", "weather / checkSunrise",
    "weather / checkSunset", "alarm / snooze_alarm", "alarm / cancel_alarm",
    "reminder / show_reminders", "reminder / cancel_reminder", "alarm / time_left_on_alarm",
    "AddToPlaylist", "BookRestaurant", "PlayMusic", "RateBook", "SearchCreativeWork",
    "SearchScreeningEvent"
]

slots = [
    "@@unkORpad@@", "O", "B-location", "I-location", "B-datetime", "I-datetime", "B-weather/attribute",
    "B-reference", "I-weather/attribute", "B-reminder/todo", "I-reminder/todo",
    "B-alarm/alarm_modifier", "B-recurring_datetime", "I-recurring_datetime", "I-reference",
    "B-reminder/reminder_modifier", "Orecurring_datetime", "B-negation", "B-timer/attributes",
    "B-news/type", "I-reminder/reminder_modifier", "B-weather/temperatureUnit",
    "I-alarm/alarm_modifier", "B-entity_name", "I-entity_name", "B-playlist", "I-playlist",
    "B-music_item", "B-artist", "I-artist", "B-party_size_number", "B-sort", "B-restaurant_type",
    "B-restaurant_name", "I-restaurant_name", "B-served_dish", "B-facility",
    "B-party_size_description", "I-party_size_description", "B-cuisine", "I-cuisine", "I-sort",
    "I-restaurant_type", "I-served_dish", "I-facility", "B-condition_temperature",
    "B-condition_description", "B-service", "I-service", "B-album", "I-album", "B-genre",
    "I-genre", "B-track", "I-track", "I-music_item", "B-rating_value", "B-best_rating",
    "B-rating_unit", "B-object_name", "I-object_name", "B-object_part_of_series_type",
    "B-object_select", "B-object_type", "I-object_select", "I-object_type",
    "I-object_part_of_series_type", "B-movie_name", "I-movie_name", "B-object_location_type",
    "I-object_location_type", "B-movie_type", "I-movie_type"
]

# Index mappings for intents and slots
intent_label_map = {i: intent for i, intent in enumerate(intents)}
slot_label_map = {i: slot for i, slot in enumerate(slots)}

def predict_own(model_dir):
    print(f"Loading model from: {model_dir}")
    # Load the model
    model = AutoModelForTokenClassification.from_pretrained(model_dir)

    print(f"Loading tokenizer from: {model_dir}")
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_dir)

    # Set the model to evaluation mode
    model.eval()

    # Example input text
    input_text = "book"

    print(f"Tokenizing input text: '{input_text}'")
    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    print(f"Input tensors shape: {inputs['input_ids'].shape}")

    # Make predictions
    with torch.no_grad():
        outputs = model(**inputs)

    # Extract logits from the model output
    logits = outputs.logits

    # Assuming logits structure: (batch_size, sequence_length, num_labels)
    # You need to adjust this based on your actual model output structure

    # Get the predicted class indices for intents and slots
    intent_predictions = torch.argmax(logits, dim=-1)[0]  # assuming single example
    slot_predictions = torch.argmax(logits, dim=-1)[0]    # assuming single example

    # Aggregate predictions to get single intent and slot
    intent_counter = Counter(intent_predictions.tolist())
    slot_counter = Counter(slot_predictions.tolist())

    # Most common intent and slot
    predicted_intent_index = intent_counter.most_common(1)[0][0]
    predicted_slot_index = slot_counter.most_common(1)[0][0]

    predicted_intent = intent_label_map[predicted_intent_index]
    predicted_slot = slot_label_map[predicted_slot_index]

    print(f"Predicted intent: {predicted_intent}")
    print(f"Predicted slot: {predicted_slot}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 predict_own.py <model_dir>")
        sys.exit(1)

    model_dir = sys.argv[1]
    predict_own(model_dir)
