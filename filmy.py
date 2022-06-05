import random
from datetime import date


class Movie:
    def __init__(self, title, year, genre, plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def play(self):
        self.plays += 1

    def __eq__(self, other):
        return self.title == other.title

    def __str__(self):
        return f"'{self.title}' ({self.year})"


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f"'{self.title}': S{self.season:02d}E{self.episode:02d}"


film1 = Movie(
    title = 'Lion King',
    year = 1994,
    genre = 'animated',
    plays = 100
)
series1 = Series(
    title = 'The Big Bang Theory',
    year = 2008,
    genre = 'comedy',
    plays = 45,
    episode = 1,
    season = 1
)
film2 = Movie(
    title = 'Pulp Fiction',
    year = 1994,
    genre = 'black comedy',
    plays = 89
)
series2 = Series(
    title = 'The Witcher',
    year = 2019,
    genre = 'fantasy',
    plays = 67,
    episode = 1,
    season = 1
)
film3 = Movie(
    title = 'The Shawshank Redemption',
    year = 1994,
    genre = 'drama',
    plays = 99    
)
series3 = Series(
    title = 'Dragon Ball Z',
    year = 1989,
    genre = 'anime',
    plays = 23,
    episode = 1,
    season = 1
)

library = [film1, series1, film2, series2, film3, series3]

def get_movies():
    movies = []
    for picture in library:
        if isinstance(picture, Series):
            continue
        movies.append(picture)
    return sorted(movies, key=lambda movie: movie.title)


def get_series():
    series = []
    for picture in library:
        if isinstance(picture, Series):
            series.append(picture)
    return sorted(series, key=lambda series: series.title)


def search(title):
    for picture in library:
        if picture.title == title:
            return picture


def generate_views():
    picture = random.choice(library)
    picture.plays = random.randint(1, 100)
    return picture.plays


def generate_views_x_10():
    for i in range(10):
        generate_views()


def top_titles(pictures_number, content_type='all'):
    if content_type == 'Movies':
        movies = []
        for picture in library:
            if isinstance(picture, Series):
                continue
            movies.append(picture)
        top_titles = sorted(
            movies,
            key=lambda movie: movie.plays,
            reverse=True
        )
        return top_titles[:pictures_number]
    elif content_type == 'Series':
        series = []
        for picture in library:
            if isinstance(picture, Series):
                series.append(picture)
        top_titles = sorted(
            series,
            key=lambda series: series.plays,
            reverse=True
        )
        return top_titles[:pictures_number]
    else:
        top_titles = sorted(
            library,
            key=lambda picture: picture.plays,
            reverse=True
        )
        return top_titles[:pictures_number]


if __name__ == '__main__':
    print("Library of films and TV shows")
    generate_views()
    print(f"The most popular films and series as of {date.today():%d.%m.%Y}:")
    for title in top_titles(3):
        print(title)