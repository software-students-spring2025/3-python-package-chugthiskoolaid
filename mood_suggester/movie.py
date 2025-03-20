import random
# Dictionary containing activity recommendations based on different moods
#Movie recommendations
MOVIE_RECOMMENDATIONS = {
    "Happy": [
        "Inside Out", 
        "La La Land", 
        "Forrest Gump", 
        "The Intouchables", 
        "The Grand Budapest Hotel",
        "Amelie",
        "The Princess Bride",
        "Singin' in the Rain",
        "Up",
        "Little Miss Sunshine",
        "The Secret Life of Walter Mitty",
        "Paddington 2",
        "The Lego Movie",
        "Ratatouille",
        "Mamma Mia!",
        "Enchanted",
        "500 Days of Summer",
        "Kiki’s Delivery Service"
    ],
    
    "Sad": [
        "The Pursuit of Happyness", 
        "Schindler's List", 
        "Manchester by the Sea", 
        "A Silent Voice", 
        "Grave of the Fireflies",
        "Inside Out",
        "Good Will Hunting",
        "About Time",
        "The Perks of Being a Wallflower",
        "Dead Poets Society",
        "A Beautiful Mind",
        "The Bucket List",
        "Eternal Sunshine of the Spotless Mind",
        "One Day",
        "Brokeback Mountain",
        "My Sister’s Keeper",
        "Requiem for a Dream",
        "The Green Mile"
    ],
    
    "Stressed": [
        "My Neighbor Totoro", 
        "The Perks of Being a Wallflower", 
        "Silver Linings Playbook", 
        "Black Swan", 
        "Joker",
        "Paddington",
        "Finding Nemo",
        "The Hundred-Foot Journey",
        "Julie & Julia",
        "The Secret Garden",
        "Chef",
        "The Peanut Butter Falcon",
        "Cast Away",
        "The Darjeeling Limited",
        "The Art of Racing in the Rain",
        "A Man Called Otto",
        "Hector and the Search for Happiness",
        "Marley & Me"
    ],
    
    "Bored": [
        "The Secret Life of Walter Mitty", 
        "Call Me by Your Name", 
        "Ponyo", 
        "Spirited Away", 
        "Before Sunrise",
        "Lost in Translation",
        "The Before Trilogy",
        "The Tree of Life",
        "A Ghost Story",
        "Into the Wild",
        "The Farewell",
        "Moonlight",
        "The Grand Budapest Hotel",
        "Cloud Atlas",
        "Waking Life",
        "Her",
        "The Man Who Knew Infinity",
        "Everything Everywhere All at Once"
    ],
    
    "Motivated": [
        "Rocky", 
        "The Social Network", 
        "Whiplash", 
        "The Pursuit of Happyness", 
        "Ford v Ferrari",
        "Moneyball",
        "Limitless",
        "The Wolf of Wall Street",
        "Rush",
        "Good Will Hunting",
        "Coach Carter",
        "Million Dollar Baby",
        "The Founder",
        "Steve Jobs",
        "The Secret",
        "Remember the Titans",
        "The Imitation Game",
        "Hidden Figures"
    ],
    
    "Angry": [
        "Joker", 
        "Fight Club", 
        "There Will Be Blood", 
        "A Clockwork Orange", 
        "John Wick",
        "Kill Bill: Vol. 1 & 2",
        "Falling Down",
        "Taxi Driver",
        "Mad Max: Fury Road",
        "Training Day",
        "The Revenant",
        "American History X",
        "Scarface",
        "V for Vendetta",
        "Nightcrawler",
        "No Country for Old Men",
        "Gladiator",
        "The Girl with the Dragon Tattoo"
    ]
}


def recommend_movie(mood: str) -> str:
    mood = mood.capitalize()  # Ensure consistency in capitalization
    return random.choice(MOVIE_RECOMMENDATIONS.get(mood, ["No recommendations available for this mood."]))