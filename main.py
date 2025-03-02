from bs4 import BeautifulSoup
import requests

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = [title.getText() for title in soup.find_all("h3", class_="title")]

movie_titles = titles[::-1]  # Creates a reversed copy

# Save to a file
with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(movie_titles))
