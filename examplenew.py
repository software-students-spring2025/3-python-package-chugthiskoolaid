from mood_suggester.movie import recommend_movie

mood = input("Enter your mood: ")
print(f"Recommended Movie: {recommend_movie(mood)}")