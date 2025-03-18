import pytest
from mood_suggester.music import recommend_music

def test_recommend_music_valid_mood():

    music = {
       "happy": ["Pop music", 
                  "Upbeat electronic music"
                  "Walking on a Dream",
                  "Good as Hell",
                  "The Nights",
                  "Put Your Records On",
                  "Can’t Stop the Feeling",
                  "September",
                  "Love Me Again"],
        "sad": ["Soft piano music", 
                "Lyrical ballads",
                "The Night We Met",
                "Fix You",
                "I Will Follow You into the Dark",
                "Lost Cause",
                "When We Were Young",
                "Wake Me Up When September Ends",
                "To Build a Home",
                "The Scientist",
                "Hard Sometimes"],
        "stressed": ["Nature sounds", 
                     "Calm instrumental music",
                     "Weightless",
                     "Sunset Lover",
                     "Holocene",
                     "Clair de Lune",
                     "River Flows in You",
                     "Bloom",
                     "Opus 23",
                     "Night Owl",
                     "Breathe Me",
                     "Saturn"],
        "bored": ["Jazz", 
                  "Rock music",
                  "Dog Days Are Over",
                  "Take a Walk",
                  "Paper Planes",
                  "Houdini",
                  "Are You Bored Yet?",
                  "Go Your Own Way",
                  "Dance, Dance",
                  "Young Folks",
                  "Shut Up and Dance",
                  "HandClap"]
    }

    for mood in music.keys():
        recommended = recommend_music(mood)
        assert recommended in music[mood]  

def test_recommend_music_invalid_mood():

    assert recommend_music("excited") == "Explore a new music genre!"
    assert recommend_music("") == "Explore a new music genre!"
    assert recommend_music("unknown") == "Explore a new music genre!"