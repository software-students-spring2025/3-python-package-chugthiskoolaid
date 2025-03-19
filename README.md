# chugthiskoolaid

## Team members

- Jess Liang: [GitHub](https://github.com/jess-liang322)  
- Yukun Dong: [GitHub](https://github.com/abccdyk)  
- Hao Yang: [GitHub](https://github.com/Hao-Yang-Hao)  
- Yifan Zhang: [GitHub](https://github.com/YifanZZZZZZ)
  
## TABLE OF CONTENTS
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
5. [Usage Examples](#usage-examples)
6. [Contributing](#contributing)

## Description
Mood Recommender is your ultimate boredom-busting, vibe-matching companion! 🎉
Whether you're feeling happy, stressed, bored, or just looking for something fun to do, this package has got you covered. 
Get personalized recommendations for activities, books, movies, and music based on your mood—because sometimes, all you need is the perfect song, a great read, or a wild adventure to turn your day around. 
Just tell us how you’re feeling, and we’ll do the rest. 
Let the good vibes roll! 😎🎶📖🎬

## PyPI Page
You can find the package here: [Mood-recommender](https://pypi.org/project/mood-recommender/)

## Installation

You can import the Mood Recommender package into your projects using pip. 
Below is how to install the package:

**1. Install the package from PyPI**
```
pip install mood-recommender
```

**2. Import the functions in your Python code**
```
from mood_suggester import recommend_activity, recommend_book, recommend_movie, recommend_music
```
## Virtual Environment & Dependencies
how to configure and run all parts of your project for any developer on any platform 
how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.
1️⃣ **Clone the Repository**
```
git clone https://github.com/software-students-spring2025/3-python-package-chugthiskoolaid.git
cd mood-suggester

```

2️⃣ **Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
```

3️⃣ **Install Dependencies**
```
pip install -r requirements.txt
```

4️⃣ **Run Tests**
```
pytest tests/
```

5️⃣ Build the Package
```
python setup.py sdist bdist_wheel
```

## Usage Examples
```
see example.py
```
## recommend_activity:
```
How are you feeling now? (happy/sad/stressed/bored/motivated/angry): bored

🎉 activity: Solve a puzzle, play a board game, or try an escape room challenge
```
## recommend_book:
```
How are you feeling now? (happy/sad/stressed/bored/motivated/angry): happy

📖 book: The Hundred-Year-Old Man Who Climbed Out the Window and Disappeared – Jonas Jonasson
```
## recommend_movie:
```
How are you feeling now? (happy/sad/stressed/bored/motivated/angry): angry

🍽 movie: The Revenant
```
## recommend_music:
```
How are you feeling now? (happy/sad/stressed/bored/motivated/angry): bored

🎵 music: Young Folks - Peter Bjorn and John
```

## Contributing  

We welcome contributions! If you would like to improve **Mood Recommender**, follow these steps:  

### 1️⃣ Fork the Repository  
Click on the **Fork** button at the top-right corner of the repository page.  

### 2️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/mood-recommender.git
cd mood-recommender
```

### 3️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```

### 5️⃣ Create a New Branch
```bash
git checkout -b feature-branch

```

### 6️⃣ Make Your Changes
```bash
git add .
git commit -m "Add new feature"

```
### 7️⃣ Push Changes
```bash
git push origin feature-branch

```

### 8️⃣ Submit a Pull Request
Go to the original repository on GitHub.
Click on Pull Requests > New Pull Request.
Select your branch and submit a Pull Request (PR) for review.

## 📜 License
This project is licensed under the MIT License. See the LICENSE.txt file for details.
