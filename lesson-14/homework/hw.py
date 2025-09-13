import json

def read_students():
    try:
        with open("students.json", "r", encoding="utf-8") as file:
            students = json.load(file)
            for student in students.get("students", []):
                print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    except FileNotFoundError:
        print("students.json file not found!")
    except json.JSONDecodeError:
        print("Error parsing students.json!")

if __name__ == "__main__":
    read_students()



import requests

def get_weather(city="Tashkent"):
    API_KEY = "YOUR_API_KEY"  
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Condition: {data['weather'][0]['description'].title()}")
    else:
        print("Error fetching weather data!")

if __name__ == "__main__":
    get_weather("Tashkent")

import json

FILE_NAME = "books.json"

def load_books():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"books": []}

def save_books(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def add_book(title, author, year):
    data = load_books()
    data["books"].append({"title": title, "author": author, "year": year})
    save_books(data)
    print("Book added successfully!")

def update_book(title, new_author=None, new_year=None):
    data = load_books()
    for book in data["books"]:
        if book["title"].lower() == title.lower():
            if new_author:
                book["author"] = new_author
            if new_year:
                book["year"] = new_year
            save_books(data)
            print("Book updated successfully!")
            return
    print("Book not found!")

def delete_book(title):
    data = load_books()
    new_books = [book for book in data["books"] if book["title"].lower() != title.lower()]
    data["books"] = new_books
    save_books(data)
    print("Book deleted successfully!")

if __name__ == "__main__":
    add_book("1984", "George Orwell", 1949)
    update_book("1984", new_year=1950)
    delete_book("1984")




import requests
import random

def recommend_movie(genre):
    API_KEY = "YOUR_API_KEY"  
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={genre}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("Search"):
            movie = random.choice(data["Search"])
            print(f"🎬 Recommended {genre.capitalize()} Movie: {movie['Title']} ({movie['Year']})")
        else:
            print("No movies found for this genre!")
    else:
        print("Error fetching movie data!")

if __name__ == "__main__":
    user_genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    recommend_movie(user_genre)

