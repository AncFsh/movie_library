

class Movie():

    def __init__(self, title, release_date, genre, views):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.views = 0

    @property
    def play(self):
        self.views += 1


class Series(Movie):

    def __init__(self, season_num, episode_num):
        super().__init__(title, release_date, genre, views)
        self.season_num = season_num
        self.episode_num = episode_num


