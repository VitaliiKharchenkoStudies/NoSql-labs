import pymongo
from pymongo import GEO2D

# Підключення до MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Дані для вставки
data = [
    {
        "name": "Central Park",
        "location": {"type": "Point", "coordinates": [-73.97, 40.77]},
        "category": "Parks"
    },
    {
        "name": "Sara D. Roosevelt Park",
        "location": {"type": "Point", "coordinates": [-73.9928, 40.7193]},
        "category": "Parks"
    },
    {
        "name": "Polo Grounds",
        "location": {"type": "Point", "coordinates": [-73.9375, 40.8303]},
        "category": "Stadiums"
    }
]

# Вставка даних у колекцію
collection.insert_many(data)

# Створення 2dsphere індексу
collection.create_index([("location", pymongo.GEOSPHERE)])

# Задаємо центральну точку та максимальну відстань
center_point = {"type": "Point", "coordinates": [-73.9667, 40.78]}
max_distance = 5000  # 5000 метрів

# Пошук елементів
nearby_elements = collection.find({
    "location": {
        "$near": {
            "$geometry": center_point,
            "$maxDistance": max_distance
        }
    }
})

for element in nearby_elements:
    print(element)

# Задаємо координати полігону
polygon_coordinates = [
    [-73, 40],
    [-74, 40],
    [-74, 41],
    [-73, 40]
]

# Пошук елементів в межах полігону
polygon_elements = collection.find({
    "location": {
        "$geoWithin": {
            "$geometry": {
                "type": "Polygon",
                "coordinates": [polygon_coordinates]
            }
        }
    }
})

for element in polygon_elements:
    print(element)
