import pytest
from mood_suggester.book import recommend_book, BOOK_RECOMMENDATIONS

def test_recommend_book():
    moods = ["Happy", "Sad", "Angry", "Anxiety", "Calm", "Motivated"]
    for mood in moods:
        book = recommend_book(mood)
        assert book in BOOK_RECOMMENDATIONS[mood]

def test_invalid_mood():
    assert recommend_book("Bored") == "No recommendations available for this mood."