import random

def recommend_music(mood: str) -> str:
    music = {
        "happy": ["Pop music", "Upbeat electronic music"],
        "sad": ["Soft piano music", "Lyrical ballads"],
        "stressed": ["Nature sounds", "Calm instrumental music"],
        "bored": ["Jazz", "Rock music"]
    }
    return random.choice(music.get(mood.lower(), ["Explore a new music genre!"]))