import pytest
from mood_suggester.activity import recommend_activity, ACTIVITY_RECOMMENDATIONS

def test_recommend_activity_valid_mood():

    """ activities = {
        "happy": ["Go for a walk in the park", "Attend a friend's party", "Try out new hobbies"],
        "sad": ["Write in a journal", "Meditate"],
        "stressed": ["Do deep breathing exercises", "Practice yoga", "Drink a hot cup of tea"],
        "bored": ["Learn a new skill", "Watch a documentary"]
    } """

    moods = ["happy", "sad", "stressed", "bored"]
    for mood in moods:
        activity = recommend_activity(mood)
        assert activity in ACTIVITY_RECOMMENDATIONS[mood]

    """ for mood in activities.keys():
        activity = recommend_activity(mood)
        assert activity in activities[mood]   """

def test_recommend_activity_invalid_mood():

    assert recommend_activity("excited") == "Try something new!"
    assert recommend_activity("") == "Try something new!"
    assert recommend_activity("unknown") == "Try something new!"