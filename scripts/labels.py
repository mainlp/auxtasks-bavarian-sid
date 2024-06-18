intents = [
    "@@unkORpad@@", "weather / find", "alarm / set_alarm", "alarm / show_alarms",
    "reminder / set_reminder", "alarm / modify_alarm", "weather / checkSunrise",
    "weather / checkSunset", "alarm / snooze_alarm", "alarm / cancel_alarm",
    "reminder / show_reminders", "reminder / cancel_reminder", "alarm / time_left_on_alarm",
    "AddToPlaylist", "BookRestaurant", "PlayMusic", "RateBook", "SearchCreativeWork",
    "SearchScreeningEvent"
]

#print(len(intents))
# is 19 - correct!

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

#print(len(slots))
# is 73 - correct