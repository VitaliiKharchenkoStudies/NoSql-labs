import pymongo

# Підключення до MongoDB (за замовчуванням на локальному хості та порті 27017)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Вибір бази даних "appdb"
db = client["appdb"]

# Створення колекції "users"
users_collection = db["users"]

# 3. Додавання користувача {"username":"andrew1","name":"Andrew","age":27}
new_user = {
    "username": "andrew1",
    "name": "Andrew",
    "age": 27
}
users_collection.insert_one(new_user)

# 4. Отримання користувача з username andrew1
query = {"username": "andrew1"}
user = users_collection.find_one(query)
if user:
    print("Знайдений користувач:")
    print(user)
else:
    print("Користувач з ім'ям користувача 'andrew1' не знайдений.")

# 5. Оновлення віку користувача з username andrew1 на 28
query = {"username": "andrew1"}
new_age = 28
result = users_collection.update_one(query, {"$set": {"age": new_age}})
if result.modified_count > 0:
    print("Вік користувача 'andrew1' оновлено на 28 років.")
else:
    print("Користувач з ім'ям користувача 'andrew1' не знайдений, тому оновлення не відбулося.")

# 6. Видалення користувача з username andrew1
query = {"username": "andrew1"}
result = users_collection.delete_one(query)
if result.deleted_count > 0:
    print("Користувач 'andrew1' був успішно видалений.")
else:
    print("Користувач з ім'ям користувача 'andrew1' не знайдений, тому видалення не відбулося.")

# 7. Отримання усіх документів у колекції users
all_users = users_collection.find()
print("Усі користувачі у колекції 'users':")
for user in all_users:
    print(user)

# Закрити підключення до MongoDB
client.close()
