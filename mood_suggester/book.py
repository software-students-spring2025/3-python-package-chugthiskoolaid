import random

BOOK_RECOMMENDATIONS = {
    "Happy": [
        "The Little Prince - Antoine de Saint-Exupéry",
        "Pride and Prejudice - Jane Austen",
        "Anne of Green Gables - L.M. Montgomery",
        "The Rosie Project - Graeme Simsion",
        "Eleanor Oliphant Is Completely Fine - Gail Honeyman"
    ],
    "Sad": [
        "The Fault in Our Stars - John Green",
        "A Man Called Ove - Fredrik Backman",
        "Me Before You - Jojo Moyes",
        "The Perks of Being a Wallflower - Stephen Chbosky",
        "Norwegian Wood - Haruki Murakami"
    ],
    "Angry": [
        "1984 - George Orwell",
        "Fahrenheit 451 - Ray Bradbury",
        "The Handmaid's Tale - Margaret Atwood",
        "The Road - Cormac McCarthy",
        "Brave New World - Aldous Huxley"
    ],
    "Anxiety": [
        "The Power of Now - Eckhart Tolle",
        "Daring Greatly - Brené Brown",
        "The Four Agreements - Don Miguel Ruiz",
        "The Gifts of Imperfection - Brené Brown",
        "Atomic Habits - James Clear"
    ],
    "Calm": [
        "The Alchemist - Paulo Coelho",
        "Tuesdays with Morrie - Mitch Albom",
        "The Tao of Pooh - Benjamin Hoff",
        "Walden - Henry David Thoreau",
        "Ikigai: The Japanese Secret to a Long and Happy Life - Héctor García"
    ],
    "Motivated": [
        "Can't Hurt Me - David Goggins",
        "The 7 Habits of Highly Effective People - Stephen R. Covey",
        "Grit - Angela Duckworth",
        "Mindset: The New Psychology of Success - Carol S. Dweck",
        "Deep Work - Cal Newport"
    ]
}

def recommend_book(mood: str) -> str:
    mood = mood.capitalize()  
    return random.choice(BOOK_RECOMMENDATIONS.get(mood, ["No recommendations available for this mood."]))
