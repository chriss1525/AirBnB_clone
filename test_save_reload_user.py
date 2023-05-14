#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


# all_objs = storage.all()
# print("-- Reloaded objects --")
# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- create new State --")
state = State()
state.name = "Nairobi"
state.save()
print(state)

print("-- Create new city --")
city = City()
city.name = "Nairobi"
city.save()
print(city)

print("-- Create new amenity --")
amenity = Amenity()
amenity.name = "Bathroom"
amenity.save()
print(amenity)

print("-- create new place --")
place = Place()
place.city_id = city.id
place.user_id = my_user.id
place.name = "Room 5"
place.description = "one bedroom flat"
place.number_rooms = 3
place.number_bathrooms = 1
place.max_guest = 2
place.price_by_night = 2500
place.latitude = 9.6
place.longitude = 0.45
place.amenity_ids = amenity.id
place.save()
print(place)

print("-- create new review --")
review1 = Review()
review1.place_id = place.id
review1.user_id = my_user.id
review1.text = "five stars! Loved the place"
review1.save()
print(review1)
