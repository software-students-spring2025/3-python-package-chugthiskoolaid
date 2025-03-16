from mood_suggester.suggestions import suggest_activity, suggest_music, suggest_food, suggest_quote

def main():
    mood = input("How are you feeling now？(happy/sad/stressed/bored): ").strip().lower()
    
    print("\n🎉 activity:", suggest_activity(mood))
    print("🎵 music:", suggest_music(mood))
    print("🍽 food:", suggest_food(mood))
    print("💡 quote:", suggest_quote(mood))

if __name__ == "__main__":
    main()