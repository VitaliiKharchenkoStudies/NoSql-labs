import redis
from collections import Counter

# Підключення до Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Отримання списку усіх користувачів
users = redis_client.keys('user:*')

# Отримання імені користувача та підрахунок кількості користувачів для кожного імені
usernames = [redis_client.json_get(user, 'username') for user in users]
username_count = Counter(usernames)

# Виведення результату
for username, count in username_count.items():
    print(f"Ім'я {username}: {count} користувачів")