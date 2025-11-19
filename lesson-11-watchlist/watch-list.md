# 🎬 Assignment: My Watchlist Enricher

## 🧩 Goal
Build a Python program that helps you manage a personal watchlist of movies and TV shows.  
Your program should let you **add new shows**, **fetch information** (summary, genre, rating) from the TVMaze API, 
**save your watchlist** to a file, and **mark shows as watched** with your own ratings.

By the end, you'll have a small but complete program that touches on everything we've learned so far:  
✅ data types, lists, dictionaries, loops, conditionals  
✅ functions, exception handling, and file I/O (JSON + CSV)  
✅ using external libraries (with a virtual environment!)

---

## 🧰 Setup Instructions

1. **Create a new folder** for your project, e.g. `lesson-11-watchlist`.

2. **Create and activate a virtual environment**:
   ```bash
   python3 -m venv watchlistenvironment
   watchlistenvironment\Scripts\activate       # On Windows
   # OR
   source watchlistenvironment/bin/activate    # On macOS/Linux
   ```

3. **Install the `requests` library** (we’ll use it to access the TVMaze API):
   ```bash
   pip install requests
   ```

4. **Create a file named** `watchlist.py` in your folder.

5. **Save your dependencies** (good practice for every project):
   ```bash
   pip freeze > requirements.txt
   ```

---

## 🌐 Example: Fetching data from the TVMaze API

Here’s a short example showing how to use the `requests` library to get show information from TVMaze:

```python
import requests

# Ask the user for a show title
title = input("Enter a TV show title: ")

# Build the URL for the API request
url = f"https://api.tvmaze.com/singlesearch/shows?q={title}"

# Send the request to the API
response = requests.get(url)

# Check if the request succeeded
if response.status_code == 200:
    data = response.json()  # Convert the response to a Python dictionary
    print(f"\nTitle: {data['name']}")
    print(f"Genres: {', '.join(data['genres'])}")
    print(f"Official Rating: {data['rating']['average']}")
    print(f"Summary: {data['summary']}")
else:
    print("Show not found or API request failed.")
```

💡 **Try it!**  
Run the script, type e.g. `Friends` or `Breaking Bad`, and you’ll see the info printed from TVMaze.

---

## 🧩 Your Tasks

### 1. Build the watchlist
- Create a list of dictionaries, where each dictionary represents a show.  
  Example:
  ```python
  {"title": "Friends", "genres": ["Comedy"], "rating": 8.8, "summary": "...", "watched": False}
  ```
- Allow the user to add shows by typing a title and fetching the info via the API.

### 2. List all shows
- Print a nicely formatted list of all shows in the watchlist, including genre and rating.

### 3. Save and load data
- Save the watchlist to a **JSON file** (e.g., `watchlist.json`) when exiting.
- When the program starts, **load** the existing file if it exists.

### 4. Handle errors
- Use `try`/`except` to catch:
  - Connection errors (e.g., no internet)
  - Missing data (e.g., show not found)
  - Invalid user input

---

## 🌟 Bonus Features

1. **Mark a show as watched**
   - Ask the user for a personal rating (1–5 stars).
   - Update the dictionary with `{"watched": True, "personal_rating": 5}`.

2. **View watched shows**
   - List all watched shows with both official and personal ratings.

3. **Export watched shows to CSV**
   - Columns: `title, genres, official_rating, personal_rating`

4. *(Optional)* Sort your watchlist by personal rating or genre before displaying it.

---

## 💾 Example User Flow

```
Welcome to My Watchlist Enricher!

1. Add a show
2. List my watchlist
3. Mark a show as watched
4. View watched shows
5. Save and exit

> 1
Enter show title: The Office
Found: The Office (Comedy, 2005–2013)
Added to your watchlist!

> 3
Enter show title to mark as watched: The Office
Your rating (1–5)? 5
Nice! The Office added to your watched list.

> 4
Watched shows:
- The Office ⭐ 5/5 (Official rating: 8.8)
```

---

## 🧠 Reflection
When you’re done, ask yourself:
- How did I use variables, loops, conditionals, and functions together?
- Where did I use error handling?
- How does saving data to JSON or CSV make my program more useful in real life?

---

**Have fun coding your Watchlist Enricher!**
You can get creative — maybe add movie posters, actors, or even episode lists later on 🚀
