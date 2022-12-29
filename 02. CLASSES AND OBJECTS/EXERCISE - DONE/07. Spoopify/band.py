from album import Album
from song import Song

class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_obj = ''
        for el in self.albums:
            if album_name == el.name:
                album_obj = el

        if album_obj == '':
            return f"Album {album_name} is not found."
        if album_obj.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album_obj)
        return f"Album {album_name} has been removed."

    def details(self):
        albums = []
        for el in self.albums:
            albums.append(el)

        result = ""
        for el in albums:
            result += f"{el.details()}"

        return f"Band {self.name}\n{result}\n"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))

track_one = Song("Black Damask", 4.35, False)
album_two = Album("Infamous", track_one)
track_two = Song("Hatefuck", 3.33, False)
print(album_two.add_song(track_two))
print(band.add_album(album_two))
print(band.details())

# 100/100
