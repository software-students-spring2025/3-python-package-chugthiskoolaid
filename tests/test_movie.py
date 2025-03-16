import pytest
from mood_suggester.movie import recommend_movie, MOVIE_RECOMMENDATIONS

def test_recommend_movie():
    moods = ["Happy", "Sad", "Angry", "Anxiety", "Calm", "Motivated"]
    for mood in moods:
        movie = recommend_movie(mood)
        assert movie in MOVIE_RECOMMENDATIONS[mood]

def test_invalid_mood():
    assert recommend_movie("Bored") == "No recommendations available for this mood."
