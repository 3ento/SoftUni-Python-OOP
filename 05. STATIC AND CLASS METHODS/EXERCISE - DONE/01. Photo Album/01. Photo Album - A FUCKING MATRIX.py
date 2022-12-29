import math

class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = []

    # @classmethod
    # def from_photos_count(cls, photos_count):
    #     pages = math.ceil(photos_count / 4)
    #     cls(pages)
    #
    # def add_photo(self, label: str):
    #     self.photos.append([label])
    #     return ...