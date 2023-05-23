class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count ={}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre= genre
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.show_song_artist(artist)
        self.show_song_genre(genre)

    @classmethod
    def add_song_to_count(cls, increament=1):
        cls.count += increament

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def show_song_artist(cls,artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist] = 1
        

    @classmethod
    def show_song_genre(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre]+=1
        else:
            cls.genre_count[genre] = 1

