# song.py
# yet again, some typing improvements have been made in Python 3.13. Let's look at the most interesting one: The new typing.ReadOnly type. It can be used to mark read-only attributes inside typed dicts. This is a great way to ensure that some key is not modified by mistake.
# $ python -m mypy song.py


from typing import ReadOnly, TypedDict

class Song(TypedDict):
   name: ReadOnly[str]
   band: ReadOnly[str]
   number_of_plays: int

def count_plays(s: Song) -> None:
   s["number_of_plays"] += 1  # OK
   s["name"] = "New Name"  # Error