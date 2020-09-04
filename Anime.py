class Anime(object):
    def __init__(self, _name, _genre, _type, _episodes, _rating, _members):
        self.Name = _name
        self.Genre = _genre
        self.Type = _type
        self.Episodes = _episodes
        self.Rating = _rating
        self.Members = _members

    @staticmethod
    def FromTuple(t):
        if len(t) != 6:
            raise Exception(f"Length of tuple should be 5 length is {len(t)}")
        else:
            return Anime(t[0], t[1], t[2], t[3], t[4], t[5])

    @staticmethod
    def FromQuery(arr):
        Anime_List = map(Anime.FromTuple, arr)
        return Anime_List

    def __str__(self):
        return f'Name: {self.Name}\n\tGenre: {self.Genre}\n\tType: {self.Type}\n\tEpisodes: {self.Episodes}\n\tAverage rating: {self.Rating}\n\tMembers: {self.Members}'
