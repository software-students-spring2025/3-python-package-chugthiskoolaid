import random


ACTIVITY_RECOMMENDATIONS = {
    "happy": ["Go for a walk in the park", 
                "Attend a friend's party", 
                "Try out new hobbies", 
                "Listen to your favorite music",
                "Try something creative",
                "Exercise or play a sport",
                "Enjoy a favorite meal, dessert, or relaxing spa day",
                "Call or meet up with a friend and spread the joy",
                "Dance, sing along, or just vibe to the beat",
                "Take a spontaneous trip",
                "Help a friend, volunteer, or surprise someone with a small gift",
                "Watch a funny movie, read jokes, or play games",
                "Write in a journal"],
    "sad": ["Write in a journal", 
            "Meditate",
            "Get fresh air to clear your mind",
            "Watch a comforting movie",
            "Share how you feel with someone who cares",
            "Practice deep breathing",
            "Draw, paint, write, or play music to channel your feelings into art",
            "A little movement, like stretching, yoga, or a short walk, can boost your mood",
            "Cuddle with a pet",
            "Watch cute animal videos"],
    "stressed": ["Do deep breathing exercises", 
                    "Practice yoga", 
                    "Drink a hot cup of tea",
                    "Go for a walk or exercise",
                    "Play calming music, nature sounds, or even white noise to create a relaxing atmosphere",
                    "Take a warm shower or bath",
                    "Disconnect from screens and take a break from social media",
                    "Watch funny movie or stand-up comedy to lighten your mood"],
    "bored": ["Learn a new skill", 
                "Watch a documentary",
                "Explore a new place and try to visit a new park",
                "Read an interesting novel",
                "Listen to a Podcast you're interested in",
                "Try out a new recipe",
                "Play an online video game",
                "Write a short story or poem",
                "Learn 10 new words",
                "Memorize a new fun fact"]
}

def recommend_activity(mood: str) -> str:
    mood = mood.capitalize()  
    return random.choice(ACTIVITY_RECOMMENDATIONS.get(mood.lower(), ["Try something new!"]))