#from tvnmaze import search_show
import requests


watch_list = []


def main():
    while True:
        print("What would you like to do?")
        print("1. Add a show")
        print("2. List my watchlist")
        print("3. Mark a show as watched")
        print("4. View watched shows")
        print("5. Export watched shows to CSV")
        print("6. Save and exit")

        user_choice = input()

        if user_choice == "1":
            add_show()
        elif user_choice == "2":
            list_watchlist()
        else:
            print("Not implemented")


def add_show():
    title = input("What would you like to add?")
    print(title)
    if not title:
        print("Please enter a valid show title.")
        return
    show = search_show(title)
    watch_list.append(show)


def list_watchlist():
    print(watch_list)
    
    
def watch_check3():
    watched = input("Have u watched this show(yes or No?")
    if watched.lower() == "yes":
        return True
    elif watched.lower() == "no":
        return False
    else:
        print("Please enter Yes or No")
        return watch_check3
    

import requests


def search_show(title):
    # Build the URL for the API request
    url = f"https://api.tvmaze.com/singlesearch/shows?q={title}"

    # Send the request to the API
    response = requests.get(url)
    print(response.json())

    # Check if the request succeeded
    if response.status_code == 200:
        data = response.json()  # Convert the response to a Python dictionary
        print(f"\nTitle: {data['name']}")
        print(f"Genres: {', '.join(data['genres'])}")
        print(f"Official Rating: {data['rating']['average']}")
        print(f"Summary: {data['summary']}")
        show = {
            'title': data['name'],
            'genres': data.get('genres', []),
            'rating': data['rating'].get('average') if data.get('rating') else None,
            'summary': data['summary'],
            'watched': False,
            'personal_rating': None
        }
        return show
    else:
        print("Show not found or API request failed.")

main()
print(watch_list[0]['title'])