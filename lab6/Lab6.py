import pymongo
from datetime import datetime

# Підключення до MongoDB та вибір колекції
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Дані для вставки
data = [
    {
        "meals": [
            {"name": "Fish", "servings": 2},
            {"name": "Pizza", "servings": 4},
            {"name": "Soup", "servings": 4},
            {"name": "Beef", "servings": 3}
        ],
        "date": datetime(2004, 9, 29, 10, 37, 45)
    },
    {
        "meals": [
            {"name": "Chicken", "servings": 2},
            {"name": "Beef", "servings": 3}
        ],
        "date": datetime(2011, 9, 3, 12, 24, 40)
    },
    {
        "meals": [
            {"name": "Fish", "servings": 3},
            {"name": "Fish", "servings": 2},
            {"name": "Fish", "servings": 1},
            {"name": "Cake", "servings": 5}
        ],
        "date": datetime(2011, 9, 3, 12, 24, 40)
    },
    {
        "meals": [
            {"name": "Fish", "servings": 4},
            {"name": "Cake", "servings": 1},
            {"name": "Fish", "servings": 5},
            {"name": "Beef", "servings": 3},
            {"name": "Beef", "servings": 2}
        ],
        "date": datetime(2014, 5, 13, 12, 47, 23)
    },
    {
        "meals": [
            {"name": "Beef", "servings": 5},
            {"name": "Spaghetti", "servings": 5},
            {"name": "Spaghetti", "servings": 4},
            {"name": "Fish", "servings": 1},
            {"name": "Fish", "servings": 5},
            {"name": "Cake", "servings": 4},
            {"name": "Beef", "servings": 3}
        ],
        "date": datetime(2010, 8, 5, 9, 11, 31)
    }
]

# Вставка даних у колекцію
collection.insert_many(data)

pipeline = [
    {
        "$unwind": "$meals"  # Розгортаємо масив meals
    },
    {
        "$project": {
            "month": {"$month": "$date"},  # Витягуємо місяць з дати
            "mealName": "$meals.name",
            "servings": "$meals.servings"
        }
    },
    {
        "$facet": {
            "totalServings": [
                {
                    "$group": {
                        "_id": {
                            "month": "$month",
                            "mealName": "$mealName"
                        },
                        "totalServings": {"$sum": "$servings"}
                    }
                },
                {
                    "$sort": {"_id.month": 1, "_id.mealName": 1}  # Сортуємо за місяцем та назвою страви
                }
            ],
            "totalOrders": [
                {
                    "$group": {
                        "_id": {
                            "month": "$month",
                            "mealName": "$mealName"
                        },
                        "count": {"$sum": 1}
                    }
                },
                {
                    "$sort": {"_id.month": 1, "_id.mealName": 1}  # Сортуємо за місяцем та назвою страви
                }
            ]
        }
    }
]

result = collection.aggregate(pipeline)

for record in result:
    print("Замовлення страв за місяць:")
    for servings_record, orders_record in zip(record["totalServings"], record["totalOrders"]):
        print(f"Місяць: {servings_record['_id']['month']}, Страва: {servings_record['_id']['mealName']}")
        print(f"Порцій: {servings_record['totalServings']}")
        print(f"Замовлень: {orders_record['count']}\n")
