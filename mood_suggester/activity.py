import random

def recommend_activity(mood: str) -> str:
    activities = {
        "happy": ["Go for a walk in the park", "Attend a friend's party", "Try out new hobbies"],
        "sad": ["Write in a journal", "Meditate"],
        "stressed": ["Do deep breathing exercises", "Practice yoga", "Drink a hot cup of tea"],
        "bored": ["Learn a new skill", "Watch a documentary"]
    }
    return random.choice(activities.get(mood.lower(), ["Try something new!"]))