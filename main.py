import random

class Movie():

    list = []
    def __init__(self, title, release_date, genre, views):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.views = 0
        Movie.list.append(self)

    def play(self):
            self.views += 1
            print(f'{self.title, self.release_date}')

    def __repr__(self):
        return f'{self.title, self.release_date, self.views}'

class Series(Movie):

    def __init__(self, title, release_date, genre, views, season_num, episode_num):
        super().__init__(title, release_date, genre, views)
        self.season_num = season_num
        self.episode_num = episode_num
    def play(self):
            self.views += 1
            print(f"{self.title} S{self.season_num}E{self.episode_num}")

    def __repr__(self):
        return f'{self.title, self.release_date} S{self.season_num}E{self.episode_num} {self.views}'


M_1 = Movie('The Shawshank Redemption', 1994, 'Drama', 0)
M_2 = Movie('The Godfather', 1972, 'Crime, Drama', 0)
M_3 = Movie('The Dark Knight', 2008, 'Action, Crime, Drama', 0)
M_4 = Movie('The Godfather: Part II', 1974, 'Crime, Drama', 0)
M_5 = Movie('12 Angry Men', 1957, 'Crime, Drama', 0)
S_1 = Series('Planet Earth II', 2016, 'Documentary', 0, 1, 1)
S_2 = Series('Planet Earth', 2006, 'Documentary', 0, 1, 2)
S_3 = Series('Breaking Bad', 2008, 'Crime, Drama, Thriller', 0, 1, 3)
S_4 = Series('Breaking Bad', 2008, 'Crime, Drama, Thriller', 0, 2, 4)
S_5 = Series('Band of Brothers', 2001, 'Drama, History, War', 0, 1, 5)

#M_5.play()
#print(M_5.views)
#S_5.play()
#print(S_5.views)
#print(Movie.list)

#part_7
def get_movies(lib):
    result = []
    for vid in lib:
        if isinstance(vid,Series) == False:
            result.append(vid)
    return sorted(result, key = lambda vid: vid.title)

#print(get_movies(Movie.list))

def get_series(lib):
    result = []
    for vid in lib:
        if isinstance(vid, Series) == True:
            result.append(vid)
    return sorted(result, key = lambda vid: vid.title)

#print(get_series(Movie.list))

#part_8

def search(lib, title):
    result = []
    for vid in lib:
        if vid.title == title:
            result.append(vid)
    if result:
        return result
    else:
        print('No movie/series on a list')

#print(search(Movie.list, 'The Godfather'))
#print(search(Movie.list, 'BBreaking Bad'))

#part_9

def generate_views(lib):
    r_movie = random.choice(lib)
    r_movie.views += random.choice(range(1,100))
    return r_movie.title, r_movie.views

#print(generate_views(Movie.list))

#part_10
def generate_10(lib):
    for i in range(10):
        print(generate_views(lib))

#jak zmodyfikować tę, albo poprzednią funkcję żeby pętla nie miała wpływu na wyświetlenia

#generate_10(Movie.list)

#part_11

def top_titles(lib):
    return sorted(lib, key=lambda vid: vid.views, reverse=True)[:3]

#print(top_titles(Movie.list))
