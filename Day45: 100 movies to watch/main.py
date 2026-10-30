import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

movie = soup.find_all(name="h3", class_="title")

movie_titles = []
for title in movie:
    movie_title = title.getText()
    movie_titles.append(movie_title)

# final_movie_titles = movie_titles.reverse()
final_movie_titles = movie_titles[::-1]

with open("movies.txt", "w") as file:
    for movie in final_movie_titles:
        file.write(f"{movie}\n")