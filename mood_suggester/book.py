import random

BOOK_RECOMMENDATIONS = {
    "Happy": [
        "The Little Prince - Antoine de Saint-Exupéry",
        "Pride and Prejudice - Jane Austen",
        "Anne of Green Gables - L.M. Montgomery",
        "The Rosie Project - Graeme Simsion",
        "Eleanor Oliphant Is Completely Fine - Gail Honeyman",
        "The Alchemist – Paulo Coelho",
        "A Man Called Ove – Fredrik Backman",
        "The Hitchhiker’s Guide to the Galaxy – Douglas Adams",
        "Little Women – Louisa May Alcott",
        "Good Omens – Terry Pratchett & Neil Gaiman",
        "The Hundred-Year-Old Man Who Climbed Out the Window and Disappeared – Jonas Jonasson"],
    
    "Sad": [
        "The Fault in Our Stars - John Green",
        "A Man Called Ove - Fredrik Backman",
        "Me Before You - Jojo Moyes",
        "The Perks of Being a Wallflower - Stephen Chbosky",
        "Norwegian Wood - Haruki Murakami",
        "The Comfort Book – Matt Haig",
        "The House in the Cerulean Sea – TJ Klune",
        "Tuesdays with Morrie – Mitch Albom",
        "Big Panda and Tiny Dragon – James Norbury",
        "The Midnight Library – Matt Haig",
        "Winnie-the-Pooh – A.A. Milne",
        "The Boy, the Mole, the Fox and the Horse – Charlie Mackesy"],
    
    "Stressed": [
        "1984 - George Orwell",
        "Fahrenheit 451 - Ray Bradbury",
        "The Handmaid's Tale - Margaret Atwood",
        "The Road - Cormac McCarthy",
        "Brave New World - Aldous Huxley",
        "The Gifts of Imperfection – Brené Brown",
        "Why We Sleep – Matthew Walker",
        "The Body Keeps the Score – Bessel van der Kolk",
        "Anger: Wisdom for Cooling the Flames – Thich Nhat Hanh",
        "The Four Agreements – Don Miguel Ruiz",
        "The Courage to Be Disliked – Ichiro Kishimi and Fumitake Koga"],
    
    "Bored": [
        "The Power of Now - Eckhart Tolle",
        "Daring Greatly - Brené Brown",
        "The Four Agreements - Don Miguel Ruiz",
        "The Gifts of Imperfection - Brené Brown",
        "Atomic Habits - James Clear",
        "Dare – Barry McDonagh",
        "Atlas of the Heart – Brené Brown",
        "The Happiness Trap – Russ Harris",
        "Reasons to Stay Alive – Matt Haig",
        "Unwinding Anxiety – Judson Brewer",
        "Don't Feed the Monkey Mind – Jennifer Shannon",
        "How to Do Nothing – Jenny Odell"],
    
    "Motivated": [
        "Atomic Habits - James Clear",
        "The 7 Habits of Highly Effective People - Stephen R. Covey",
        "Grit: The Power of Passion and Perseverance - Angela Duckworth",
        "Can’t Hurt Me - David Goggins",
        "The Power of Now - Eckhart Tolle",
        "The Obstacle Is the Way - Ryan Holiday",
        "Mindset: The New Psychology of Success - Carol S. Dweck",
        "Deep Work - Cal Newport",
        "The War of Art - Steven Pressfield",
        "Start with Why - Simon Sinek"],
    
    "Angry": [
        "The Dance of Anger - Harriet Lerner",
        "Why Zebras Don’t Get Ulcers - Robert Sapolsky",
        "The Body Keeps the Score - Bessel van der Kolk",
        "Radical Acceptance - Tara Brach",
        "Burnout: The Secret to Unlocking the Stress Cycle - Emily Nagoski & Amelia Nagoski",
        "Anger: Wisdom for Cooling the Flames - Thich Nhat Hanh",
        "The Gifts of Imperfection - Brené Brown",
        "The Subtle Art of Not Giving a F*ck - Mark Manson",
        "How to Win Friends and Influence People - Dale Carnegie",
        "Unfu*k Yourself - Gary John Bishop"]
}

def recommend_book(mood: str) -> str:
    mood = mood.capitalize()  
    return random.choice(BOOK_RECOMMENDATIONS.get(mood, ["No recommendations available for this mood."]))