import random

# Dictionary containing activity recommendations based on different moods
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
                 "Watch a funny movie or stand-up comedy to lighten your mood",
                 "Try aromatherapy with lavender or chamomile scents",
                 "Write down what's stressing you and break it into smaller, manageable steps"],
    "bored": ["Try out a new hobby like painting, knitting, or photography", 
              "Learn a new skill through an online course or tutorial",
              "Read a book or listen to an audiobook",
              "Cook or bake something new and experiment with different recipes",
              "Explore a new place in your city or take a spontaneous road trip",
              "Solve a puzzle, play a board game, or try an escape room challenge",
              "Write a short story, poem, or start a blog",
              "Declutter and reorganize your room for a fresh start",
              "Volunteer for a local cause or help someone in need",
              "Challenge yourself with a DIY project or build something creative"],
    "motivated": ["Set a new goal and plan out the steps to achieve it", 
                  "Hit the gym or do an intense workout",
                  "Read an inspiring book or listen to a motivational podcast",
                  "Write down affirmations or visualize your success",
                  "Work on a passion project or learn a new skill",
                  "Surround yourself with like-minded, driven people",
                  "Watch TED talks or success stories to fuel your drive",
                  "Organize your workspace and create a productive environment"],
    "angry": ["Do a high-intensity workout or go for a run", 
              "Write down your thoughts, then tear up the paper or burn it safely", 
              "Listen to aggressive music or play an instrument to release tension",
              "Practice controlled breathing exercises",
              "Hit a punching bag or squeeze a stress ball",
              "Take a cold shower to reset your emotions",
              "Talk it out with someone you trust",
              "Engage in a creative activity like painting, writing, or playing a video game to redirect your energy"]

}
"""
    Given a mood, recommend a random book from the corresponding category.

    Parameters:
        mood (str): The user's current mood.
    
    Returns:
        str: A recommended book title.
"""

def recommend_activity(mood: str) -> str:
    mood = mood.capitalize()  # Ensure consistency in capitalization
    return random.choice(ACTIVITY_RECOMMENDATIONS.get(mood.lower(), ["Try something new!"]))