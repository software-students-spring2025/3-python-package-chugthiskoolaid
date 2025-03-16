import pytest
from mood_suggester.music import recommend_music

def test_recommend_music_valid_mood():

    music = {
        "happy": ["Pop music", "Upbeat electronic music"],
        "sad": ["Soft piano music", "Lyrical ballads"],
        "stressed": ["Nature sounds", "Calm instrumental music"],
        "bored": ["Jazz", "Rock music"]
    }

    for mood in music.keys():
        recommended = recommend_music(mood)
        assert recommended in music[mood]  

def test_recommend_music_invalid_mood():

    assert recommend_music("excited") == "Explore a new music genre!"
    assert recommend_music("") == "Explore a new music genre!"
    assert recommend_music("unknown") == "Explore a new music genre!"