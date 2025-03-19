import random
from mood_suggester import activity, book, movie, music

def main():
    # Define categories
    categories = {
        "🎉 activity": activity.recommend_activity,
        "🎵 music": music.recommend_music,
        "🍽 movie": movie.recommend_movie,
        "📖 book": book.recommend_book
    }
    # Randomly select one category
    selected_category, recommend_function = random.choice(list(categories.items()))
    if "activity" in selected_category:
        print("Feeling restless?  Inspired?  Maybe a little down?  Not sure what to do? Let your emotions guide you! No worries—I have just the right activity to match your mood and help you make the most of your day!")
    elif "music" in selected_category:
        print("Music speaks when words can’t. Every mood has a melody to match. Tell me how you're feeling, and I'll find the perfect song to match your vibe and emotions!")
    elif "movie" in selected_category:
        print("Looking for a movie that fits your emotions? Whether you're in the mood for action, romance, or something uplifting, I’ve got a perfect recommendation just for you!")
    elif "book" in selected_category:
        print("Books have a unique way of reflecting and shaping our emotions.  Whether you're feeling adventurous and craving an epic journey, or simply looking for a heartwarming story to lift your spirits, there’s a perfect book waiting for you.  Tell me how you're feeling, and I'll recommend a story that resonates with your mood and transports you to the world you need most right now!")

    mood = input("How are you feeling now? (happy/sad/stressed/bored/motivated/angry): ").strip().lower()

    # Generate and display a recommendation from the selected category
    print(f"{selected_category}: {recommend_function(mood)}")


if __name__ == "__main__":
    main()
