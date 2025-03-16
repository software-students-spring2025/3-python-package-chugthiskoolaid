import random

#Move recommendations
MOVIE_RECOMMENDATIONS = {
    "Happy": ["Inside Out", "La La Land", "Forrest Gump", "The Intouchables", "The Grand Budapest Hotel"],
    "Sad": ["The Pursuit of Happyness", "Schindler's List", "Manchester by the Sea", "A Silent Voice", "Grave of the Fireflies"],
    "Angry": ["John Wick", "Mad Max: Fury Road", "Fight Club", "Gladiator", "The Dark Knight"],
    "Anxiety": ["A Beautiful Mind", "The Perks of Being a Wallflower", "Silver Linings Playbook", "Black Swan", "Joker"],
    "Calm": ["The Secret Life of Walter Mitty", "Amélie", "Ponyo", "Spirited Away", "Before Sunrise"],
    "Motivated": ["Rocky", "The Social Network", "Whiplash", "The Wolf of Wall Street", "Good Will Hunting"]
}

def recommend_movie(mood: str) -> str:
    mood = mood.capitalize()  
    return random.choice(MOVIE_RECOMMENDATIONS.get(mood, ["No recommendations available for this mood."]))