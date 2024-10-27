from typing_extensions import ReadOnly
from typing import TypedDict

class Song(TypedDict):
    name: ReadOnly[str]
    artist: ReadOnly[str]

# Creating an instance
my_song: Song = {"name": "Imagine", "artist": "John Lennon"}
print(my_song["name"])   # Output: Imagine
print(my_song["artist"]) # Output: John Lennon

my_song["name"]= "Sincar"

print(my_song["name"]) # 