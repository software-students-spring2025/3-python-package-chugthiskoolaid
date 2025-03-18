import pytest
from mood_suggester.book import recommend_book, BOOK_RECOMMENDATIONS

def test_recommend_book():
    moods = ["happy", "sad", "stressed", "bored"，"motivated","angry"]
    for mood in moods:
        book = recommend_book(mood)
        assert book in BOOK_RECOMMENDATIONS[mood]

def test_invalid_mood():
    assert recommend_book("") == "No recommendations available for this mood."