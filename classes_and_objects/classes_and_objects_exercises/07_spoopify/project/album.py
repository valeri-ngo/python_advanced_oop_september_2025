from project.song import Song


class Album:

    def __init__(self, name: str, published = False):
        self.name = name
        self.published: bool = published
        self.songs: list = []

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        for s in self.songs:
            if s.name == song.name:
                return "Song is already in the album."

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_to_remove = None

        if self.published:
            return "Cannot remove songs. Album is published."

        for s in self.songs:
            if s.name == song_name:
                song_to_remove = s
                break

        if song_to_remove is None:
            return "Song is not in the album."

        self.songs.remove(song_to_remove)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"

        for song in self.songs:
            result += f"== {song.get_info()}\n"

        return result