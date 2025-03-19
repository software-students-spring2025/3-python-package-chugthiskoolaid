from mood_suggester import activity, book, movie, music

def main():
    mood = input("How are you feeling now？(happy/sad/stressed/bored): ").strip().lower()
    
    print("\n🎉 activity:", activity.recommend_activity(mood))
    print("🎵 music:", music.recommend_music(mood))
    print("🍽 movie:", movie.recommend_movie(mood))
    print("💡 book:", book.recommend_book(mood))

if __name__ == "__main__":
    main()
