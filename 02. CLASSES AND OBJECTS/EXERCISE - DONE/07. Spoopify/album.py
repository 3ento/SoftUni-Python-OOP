from song import Song

class Album:
    def __init__(self, name: str, songs=None):
        self.name = name
        if songs is None:
            self.songs = []
        else:
            self.songs = [songs]
        self.published = False

    def add_song(self, song: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        # hopefully a reliable way to get the object from its name
        song_obj = ''
        for el in self.songs:
            if song_name == el.name:
                song_obj = el

        # if the song_obj is still empty, it means the for cycle didn't find matches with the input, meaning the element is not in the list
        if song_obj == '':
            return "Song is not in the album."
        if self.published:
            return "Cannot remove songs. Album is published."
        self.songs.remove(song_obj)
        return f"Removed song {song_name} from album {self.name}."


    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = ''
        for el in self.songs:
            result += f"== {el.get_info()}\n"

        return f"Album {self.name}\n{result}"

# 100/100





