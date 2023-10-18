# Лабораторна робота 5 Харченко Віталій ІКМ-223Б

Для виконання цих завдань, потрібно спершу підключитися до MongoDB бази даних з використанням Python та бібліотеки
PyMongo.

### Завдання 1. Створіть колекцію з валідатором JSON схеми:

#### Рішення:

```python
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
```

### Завдання 2. Збережіть дані до колекції:

#### Рішення:

```python
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
```

### Завдання 3. Створіть індекс з полем "модель процесору":

#### Рішення:

```python
collection.create_index([("processor.model", 1)])
```

### Завдання 4. Отримайте усі комп'ютери з 8 ядерними процесорами:

#### Рішення:

```python
computers_with_8_cores = collection.find({"processor.cores": 8})
for computer in computers_with_8_cores:
    print(computer)
```

### Завдання 5. Отримайте усі комп'ютери Lenovo з процесором 5800h:

#### Рішення:

```python
lenovo_computers_with_5800h = collection.find({"vendor": "Lenovo", "processor.model": "5800h"})
for computer in lenovo_computers_with_5800h:
    print(computer)
```

### Завдання 6. Створіть текстовий індекс з полями "type" та "vendor":

#### Рішення:

```python
collection.create_index([("type", "text"), ("vendor", "text")])
```

### Завдання 7. За допомогою текстового індексу знайдіть комп'ютери за пошуком "laptops":

#### Рішення:

```python
laptops = collection.find({"$text": {"$search": "laptops"}})
for laptop in laptops:
    print(laptop)
```
![Вивід консолі](https://media.discordapp.net/attachments/917547349864230912/1164296655026262158/image.png?ex=6542b2c2&is=65303dc2&hm=43a7def17b2dd5e49daacf830fad1df48d60b3d091f290c0b03aaa53ecd0da3f&=&width=1440&height=303)
