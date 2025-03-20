import random
# This script provides music recommendations based on the user's mood.
# Users input a mood, and the program suggests a song matching the feeling.

# Dictionary containing categorized music recommendations.
# Each mood is associated with a list of songs that reflect its emotional vibe.

# Function to recommend a song based on the user's mood.
# It randomly selects a track from the corresponding category.
# Dictionary containing activity recommendations based on different moods
music = {
    "happy": ["Pop music", 
              "Upbeat electronic music",
              "Walking on a Dream - Empire of the Sun",
              "Good as Hell - Lizzo",
              "The Nights - Avicii",
              "Put Your Records On - Corinne Bailey Rae",
              "Can’t Stop the Feeling - Justin Timberlake",
              "September - Earth, Wind & Fire",
              "Love Me Again - John Newman",
                "Happy - Pharrell Williams",
                "Shut Up and Dance - WALK THE MOON",
            "Uptown Funk - Mark Ronson ft. Bruno Mars",
            "Electric Feel - MGMT",
            "Blinding Lights - The Weeknd",
            "Sugar - Maroon 5",
            "On Top of the World - Imagine Dragons",
            "Good Day - Nappy Roots"],

    "sad": ["Soft piano music", 
            "Lyrical ballads",
            "The Night We Met - Lord Huron",
            "Fix You - Coldplay",
            "I Will Follow You into the Dark - Death Cab for Cutie",
            "Lost Cause - Billie Eilish",
            "When We Were Young - Adele",
            "Wake Me Up When September Ends - Green Day",
            "To Build a Home - The Cinematic Orchestra",
            "The Scientist - Coldplay",
            "Hard Sometimes - Ruel",
            "Someone Like You - Adele",
        "Breathe Me - Sia",
        "Je te laisserai des mots - Patrick Watson",
        "Skinny Love - Bon Iver",
        "Iris - Goo Goo Dolls",
        "Creep (Acoustic) - Radiohead",
        "All I Want - Kodaline"],

    "stressed": ["Nature sounds", 
                 "Calm instrumental music",
                 "Weightless - Marconi Union",
                 "Sunset Lover - Petit Biscuit",
                 "Holocene - Bon Iver",
                 "Clair de Lune - Claude Debussy",
                 "River Flows in You - Yiruma",
                 "Bloom - The Paper Kites",
                 "Opus 23 - Dustin O'Halloran",
                 "Night Owl - Galimatias",
                 "Breathe Me - Sia",
                 "Saturn - Sleeping at Last",
                 "Einaudi: Nuvole Bianche - Ludovico Einaudi",
        "First Love - Hikaru Utada",
        "Mystery of Love - Sufjan Stevens",
        "La Vie en Rose - Édith Piaf",
        "Lost in Japan (Acoustic) - Shawn Mendes",
        "Cold Little Heart - Michael Kiwanuka"],

    "bored": ["Jazz", 
              "Rock music",
              "Dog Days Are Over - Florence + The Machine",
              "Take a Walk - Passion Pit",
              "Paper Planes - M.I.A.",
              "Houdini - Foster the People",
              "Are You Bored Yet? - Wallows ft. Clairo",
              "Go Your Own Way - Fleetwood Mac",
              "Dance, Dance - Fall Out Boy",
              "Young Folks - Peter Bjorn and John",
              "Shut Up and Dance - WALK THE MOON",
              "HandClap - Fitz and The Tantrums",
              "Tongue Tied - Grouplove",
        "Take It Easy - Eagles",
        "Float On - Modest Mouse",
        "Do I Wanna Know? - Arctic Monkeys",
        "Electric Love - BØRNS",
        "Bad Habit - Steve Lacy"],
    
    "motivated": ["Eye of the Tiger", 
                  "Stronger - Kanye West", 
                  "Lose Yourself - Eminem", 
                  "We Will Rock You - Queen", 
                  "Can't Hold Us - Macklemore & Ryan Lewis", 
                  "Till I Collapse - Eminem", 
                  "Remember the Name - Fort Minor", 
                  "Unstoppable - Sia", 
                  "Hall of Fame - The Script", 
                  "Born to Run - Bruce Springsteen",
                  "Survivor - Destiny's Child",
        "Don't Stop Believin' - Journey",
        "Roar - Katy Perry",
        "Believer - Imagine Dragons",
        "Defying Gravity - Idina Menzel",
        "Thunderstruck - AC/DC",
        "Started from the Bottom - Drake"],

    "angry": ["Break Stuff - Limp Bizkit", 
              "Killing in the Name - Rage Against the Machine", 
              "Smells Like Teen Spirit - Nirvana", 
              "Duality - Slipknot", 
              "Bodies - Drowning Pool", 
              "Headstrong - Trapt", 
              "The Way I Am - Eminem", 
              "Before I Forget - Slipknot", 
              "Down with the Sickness - Disturbed", 
              "Psychosocial - Slipknot",
              "My Own Summer (Shove It) - Deftones",
        "Freak on a Leash - Korn",
        "No More Tears - Ozzy Osbourne",
        "Sabotage - Beastie Boys",
        "Break - Three Days Grace",
        "Stressed Out - Twenty One Pilots",
        "Monster - Skillet",
        "Given Up - Linkin Park"]
}


def recommend_music(mood: str) -> str:
    mood = mood.capitalize()  # Ensure consistency in capitalization
    return random.choice(music.get(mood.lower(), ["Explore a new music genre!"]))