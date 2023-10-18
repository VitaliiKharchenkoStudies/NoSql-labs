from pymongo import MongoClient

# Підключення до бази даних
client = MongoClient('mongodb://localhost:27017')
db = client['mydatabase']
collection = db['computers']

# Валідатор JSON схеми
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["type", "vendor"],
        "properties": {
            "type": {
                "enum": ["DESKTOP", "LAPTOP"]
            },
            "vendor": {
                "bsonType": "string"
            }
        }
    }
}

# Створення колекції з валідатором
collection.create_index([("type", 1), ("vendor", 1)], unique=True)


data = [
    {
        "type": "LAPTOP",
        "vendor": "Lenovo",
        "processor": {
            "manufacturer": "AMD",
            "cores": 8,
            "model": "5800h"
        }
    },
    {
        "type": "DESKTOP",
        "vendor": "Dell",
        "processor": {
            "manufacturer": "Intel",
            "cores": 16,
            "model": "12900k"
        },
    },
    {
        "type": "LAPTOP",
        "vendor": "Asus",
        "processor": {
            "manufacturer": "AMD",
            "cores": 8,
            "model": "5800h"
        },
    },
    {
        "type": "LAPTOP",
        "vendor": "Apple",
        "processor": {
            "manufacturer": "Apple",
            "cores": 8,
            "model": "M1"
        },
    }
]

# Додавання даних до колекції
try:
    collection.insert_many(data)
except:
    print("Дані вже існують")

collection.create_index([("processor.model", 1)])


computers_with_8_cores = collection.find({"processor.cores": 8})
print("Результат запиту computers_with_8_cores:")
for computer in computers_with_8_cores:
    print(computer)

lenovo_computers_with_5800h = collection.find({"vendor": "Lenovo", "processor.model": "5800h"})
print("Результат запиту lenovo_computers_with_5800h:")
for computer in lenovo_computers_with_5800h:
    print(computer)

collection.create_index([("type", "text"), ("vendor", "text")])


laptops = collection.find({"$text": {"$search": "laptops"}})
print("Результат запиту laptops:")
for laptop in laptops:
    print(laptop)
