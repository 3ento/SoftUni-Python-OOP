from project.room import Room
import unittest

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, star_count):
        return cls(f"{star_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = ''
        for el in self.rooms:
            if el.number == room_number:
                room = el

        if not room.capacity < people and not room.is_taken:
            room.guests += people
            self.guests += people
            room.is_taken = True

    def free_room(self, room_number):
        room = ''
        for el in self.rooms:
            if el.number == room_number:
                room = el

        if not room.is_taken:
            return f"Room number {room.number} is not taken"

        room.is_taken = False
        self.guests -= room.guests
        room.guests = 0

    def status(self):
        free_rooms = []
        taken_rooms = []
        sep = ", "

        for el in self.rooms:
            if el.is_taken:
                taken_rooms.append(str(el.number))
            else:
                free_rooms.append(str(el.number))

        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms: {sep.join(free_rooms)}\nTaken rooms: {sep.join(taken_rooms)}"

# 82/100
# 91/100
# 100/100
