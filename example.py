import random
from mood_suggester import activity, book, movie, music

def main():
    mood = input("How are you feeling now? (happy/sad/stressed/bored/motivated/angry): ").strip().lower()
    
    # Define categories
    categories = {
        "🎉 activity": activity.recommend_activity,
        "🎵 music": music.recommend_music,
        "🍽 movie": movie.recommend_movie,
        "📖 book": book.recommend_book
    }
    
    # Randomly select one category
    selected_category, recommend_function = random.choice(list(categories.items()))
    
    # Generate and display a recommendation from the selected category
    print(f"\n{selected_category}: {recommend_function(mood)}")


if __name__ == "__main__":
    main()
