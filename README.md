# chugthiskoolaid

Team members: Hao Yang, Yukun Dong, Jess, YifanZzzz

## TABLE OF CONTENTS
1. [Description](#description)
2. [PyPI Page](#pypi-page)
3. [Installation](#installation)
4. [Virtual Environment & Dependencies](#virtual-environment--dependencies)
5. [Usage Examples](#usage-examples)
6. [Contributing](#contributing)

## Description
A package that generates “Mood Suggester” messages, programming wisdom, or absurd advice when called.

## PyPI Page
You can find the package here:

## Installation

You can import the Mood Suggester package into your projects using pip. Below is how to install the package:

**1. Install the package from PyPI**
```
pip install mood_suggester
```

**2. Import the functions in your Python code**
```
from mood_suggester import recommend_activity, recommend_book, recommend_movie, recommend_music
```
## Virtual Environment & Dependencies
how to configure and run all parts of your project for any developer on any platform 
how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.
1️⃣ Clone the Repository
```
git clone https://github.com/software-students-spring2025/3-python-package-chugthiskoolaid/tree/main
cd mood-suggester
```

2️⃣ Create a Virtual Environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

4️⃣ Run Tests
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
**1. recommend_activity**
```
user_input = input("Enter a word, phrase, or thought to receive your fortune: ")
print(get_fortune(user_input))
```
**2. recommend_book**

**3. recommend_movie**

**4. recommend_music**

## Contributing
We welcome contributions! Here’s how you can help:

