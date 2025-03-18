import pytest
from mood_suggester.activity import recommend_activity, ACTIVITY_RECOMMENDATIONS

def test_recommend_activity_valid_mood():

    """ activities = {
        "happy": ["Go for a walk in the park", "Attend a friend's party", "Try out new hobbies"],
        "sad": ["Write in a journal", "Meditate"],
        "stressed": ["Do deep breathing exercises", "Practice yoga", "Drink a hot cup of tea"],
        "bored": ["Learn a new skill", "Watch a documentary"]
        "motivated": ["Set a new goal and plan out the steps to achieve it", 
                  "Hit the gym or do an intense workout"]
        "angry": ["Do a high-intensity workout or go for a run", 
              "Write down your thoughts, then tear up the paper or burn it safely"]} 
    """

    moods = ["happy", "sad", "stressed", "bored", "motivated","angry"]
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