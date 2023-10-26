# Лабораторна робота 6 Харченко Віталій ІКМ-223Б

### Завдання 1. Збережіть наступні дані до MongoDB колекції

1. **Підключення до MongoDB та вибір колекції:**
   ```python
   client = pymongo.MongoClient("mongodb://localhost:27017/")
   db = client["mydatabase"]
   collection = db["mycollection"]
   ```
   У цьому розділі коду створюється підключення до бази даних MongoDB, вибирається конкретна база даних (`mydatabase`) та колекція (`mycollection`), з якою буде працювати програма.

2. **Дані для вставки:**
   ```python
   data = [
       # ... (список об'єктів з даними для вставки)
   ]
   ```
   В цьому розділі коду міститься список об'єктів, які будуть вставлені у колекцію. Кожен об'єкт містить дані про прийоми їжі та дату.

3. **Вставка даних у колекцію:**
   ```python
   collection.insert_many(data)
   ```
   Ця операція вставляє дані у вибрану колекцію.

### Завдання 2. За допомогою MongoDB агрегацій порахуйте скільки порцій кожної страви за кожний місяць було замовлено (дані повинні бути відсортовані за датою замовлення)
### Завдання 3. За допомогою MongoDB агрегацій порахуйте скільки разів кожна страва за кожний місяць була замовлена (дані повинні бути відсортовані за датою замовлення
 
2. **Агрегація даних:**
   ```python
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
     }]  result = collection.aggregate(pipeline)
  ```У цьому розділі коду створюється конвеєр агрегації, який обробляє дані в колекції. Потім виконується агрегація за допомогою методу `aggregate`, і результат записується у змінну `result`.

5. **Виведення результатів:**
   ```python  
   for record in result:
      print("Замовлення страв за місяць:")
     for servings_record, orders_record in zip(record["totalServings"], record["totalOrders"]):
        print(f"Місяць: {servings_record['_id']['month']}, Страва: {servings_record['_id']['mealName']}")
        print(f"Порцій: {servings_record['totalServings']}")
        print(f"Замовлень: {orders_record['count']}\n")
   ```
   У цьому розділі коду виводяться результати агрегації, включаючи місяць, назву страви, кількість порцій та кількість замовлень.
![alt](https://media.discordapp.net/attachments/917547349864230912/1167203947547725894/image.png?ex=654d4662&is=653ad162&hm=b599834b457948b5d160d7e5c1de578f713508bc025231b16e82dc79bc1d1c46&=&width=332&height=670)