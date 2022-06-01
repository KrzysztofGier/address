import random
from datetime import date


class Films:
    def __init__(self, title, year, genre, plays):
        self.title = title # tytuł
        self.year = year #rok wydania
        self.genre = genre #gatunek
        self.plays = plays #Liczba odtworzeń


        #Variables
        self._no_plays = 0


    def __str__(self):
        return f'{self.title}, ({self.year})'    
    def __repr__(self):
        return f" title = {self.title} year = {self.year}"

    @property
    def current_no_plays(self):
        return self._no_plays

    @current_no_plays.setter
    def current_no_plays(self, value):
        self._no_plays = value


    def next_play(self, step =1): #Zwiększenie liczby odtworzeń o "step"
        self.current_no_plays += step
        print(f'Liczba odtworzeń {self.title} zwiększyła się o {step}')  
        
       

film1 = Films(title = "Shrek", year ="2001", genre ="Bajka", plays = 0)
film2 = Films(title = "Legion samobójców", year = "2021", genre = "Akcja", plays = 0)
film3 = Films(title = "Wyprawa do dżungi", year = "2021", genre = "Fantasy", plays = 0)
film4 = Films(title = "Skazani na Shawshank", year = "1994", genre = "Dramat", plays = 0)
film5 = Films(title = "Nietykalni", year = "2011", genre = "Biografdiczny/Dramat/Komedia", plays = 0)
film_list = [film1, film2, film3, film4, film5]


class Series(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    
        #Variables
        self.episode = format(episode,'02d')  #zapis w forime dwucyfrowej 01 etc
        self.season = format(season, '02d')
    def __str__(self):
        return f'{self.title}, S{self.season}E{self.episode}'

series1 = Series(title = "Teoria wielkiego podrywu", year = "2007 - 2019", genre = "Sictom",plays = 0, episode = 0, season= 0)
series2 = Series(title ="Jak poznałem waszą matkę", year = "2005 - 2014", genre="Sitcom",plays = 0, episode = 0, season= 0)
series3 = Series(title = "Dr House", year = "2004 - 2012", genre = "Drama",plays = 0, episode = 0, season= 0)
series4 = Series(title = "Przyjaciele", year = "1994 - 2004", genre = "Sitcom",plays = 0, episode = 0, season= 0)
series5 = Series(title = "The 100", year = "2014 - " , genre = "Science - Fiction",plays = 0, episode = 0, season= 0)
series_list = [series1, series2, series3, series4, series5]




Library_list = film_list + series_list 
class Library: #Klasa dla filmów i seriali
    
    def __init__(self):
        self._database = []

    @property
    def database(self):
        return self._database
    
    def add(self, film_or_series):
        self._database.append(film_or_series)

        

    def get_movies(self):
        by_title = sorted(film_list, key=lambda film: film.title) #sortowanie
        print(by_title)



    def get_series(self):
        by_title = sorted(series_list, key=lambda series: series.title) #sortowanie
        print(by_title)

    def search(self,title):
        for item in self._database:
            if item.title == title:
                return item


    def generate_views():
        item  = random.choice(Library_list) #Losowy film/serial
        item.plays = random.randint(1,100) #Losowa liczba odtworzeń
        return item.plays
        

    def generate_views_x10():
        for i in range(10):
            Library.generate_views()


    def top_titles(titles_number, content_type='all'):
        if content_type == 'Films':
            films = []
            for item in film_list:
                if isinstance(item, Series):
                    continue
                films.append(item)
            top_titles = sorted(films,key=lambda films: films.plays)
            return top_titles[:titles_number]
        elif content_type == 'Series':
            series = []
            for item in series_list:
                if isinstance(item, Series):
                    series.append(item)
            top_titles = sorted(series, key=lambda series: series.plays)
            return top_titles[:titles_number]
        else:
            top_titles = sorted(film_list, key=lambda titles: titles.plays, reverse = True)
        return top_titles[:titles_number]


if __name__ == '__main__':
    print("Biblioteka filmów i seriali")
    Library.generate_views()
    print(f'Najbardziej popularne filmy i seriale na dziś to {date.today(): %d.%m.%y}: ')
    for title in Library.top_titles(3):
        print(title)



#Kompletna bibliotka "library" dla _database 
library = Library()
library.add(film1)
library.add(film2)
library.add(film3)
library.add(film4)
library.add(film5)
library.add(series1)  
library.add(series2)
library.add(series3)
library.add(series4)
library.add(series5) 