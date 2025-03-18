import pytest
from mood_suggester.music import recommend_music

def test_recommend_music_valid_mood():

    music = {
        "happy": ["Pop music", 
                "Upbeat electronic music",
                "Walking on a Dream - Empire of the Sun",
                "Good as Hell - Lizzo",
                "The Nights - Avicii",
                "Put Your Records On - Corinne Bailey Rae",
                "Can’t Stop the Feeling - Justin Timberlake",
                "September - Earth, Wind & Fire",
                "Love Me Again - John Newman"],

        "sad": ["Soft piano music", 
                "Lyrical ballads",
                "The Night We Met - Lord Huron",
                "Fix You - Coldplay",
                "I Will Follow You into the Dark - Death Cab for Cutie",
                "Lost Cause - Billie Eilish",
                "When We Were Young - Adele",
                "Wake Me Up When September Ends - Green Day",
                "To Build a Home - The Cinematic Orchestra",
                "The Scientist - Coldplay",
                "Hard Sometimes - Ruel"],

        "stressed": ["Nature sounds", 
                    "Calm instrumental music",
                    "Weightless - Marconi Union",
                    "Sunset Lover - Petit Biscuit",
                    "Holocene - Bon Iver",
                    "Clair de Lune - Claude Debussy",
                    "River Flows in You - Yiruma",
                    "Bloom - The Paper Kites",
                    "Opus 23 - Dustin O'Halloran",
                    "Night Owl - Galimatias",
                    "Breathe Me - Sia",
                    "Saturn - Sleeping at Last"],

        "bored": ["Jazz", 
                "Rock music",
                "Dog Days Are Over - Florence + The Machine",
                "Take a Walk - Passion Pit",
                "Paper Planes - M.I.A.",
                "Houdini - Foster the People",
                "Are You Bored Yet? - Wallows ft. Clairo",
                "Go Your Own Way - Fleetwood Mac",
                "Dance, Dance - Fall Out Boy",
                "Young Folks - Peter Bjorn and John",
                "Shut Up and Dance - WALK THE MOON",
                "HandClap - Fitz and The Tantrums"],
    }

    for mood in music.keys():
        recommended = recommend_music(mood)
        assert recommended in music[mood]  

def test_recommend_music_invalid_mood():

    assert recommend_music("excited") == "Explore a new music genre!"
    assert recommend_music("") == "Explore a new music genre!"
    assert recommend_music("unknown") == "Explore a new music genre!"