# Лабораторна робота 10 Харченко Віталій ІКМ-223Б

### Встановлення

Перш ніж почати, переконайтеся, що у вас встановлено бібліотеку Neo4j для Python:

```bash
pip install neo4j
```

### Підключення до Neo4j

Для початку роботи з базою даних Neo4j, створить об'єкт `Neo4jConnection` та використає його для встановлення з'єднання:

```python
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
username = "lodkidb"
password = "Fs[R91-<Q7.5"

class Neo4jConnection:
    def __init__(self, uri, username, password):
        self._uri = uri
        self._username = username
        self._password = password
        self._driver = None

    def close(self):
        if self._driver is not None:
            self._driver.close()

    def connect(self):
        self._driver = GraphDatabase.driver(self._uri, auth=(self._username, self._password))
        return self._driver
```

### Використання та Запити

Далі визначте функцію `create_and_query_data`, яка виконує різні операції з базою даних Neo4j:

```python
def create_and_query_data(tx):
    # 1. Створення ноди
    tx.run("CREATE (:Person {name: 'Mariia'})")
    tx.run("CREATE (:Person {name: 'Mark'})")

    # 2. Створення зв'язку
    tx.run("MATCH (mariia:Person {name: 'Mariia'}), (mark:Person {name: 'Mark'}) "
           "CREATE (mariia)-[:LOVES]->(mark)")

    # 3. Виведення графа
    result = tx.run("MATCH (n) RETURN n")
    for record in result:
        print(record)

    # 4. Видалення зв'язку
    tx.run("MATCH (:Person {name: 'Mariia'})-[r:LOVES]-(:Person {name: 'Mark'}) DELETE r")

    # 5. Видалення нод
    tx.run("MATCH (n:Person) DELETE n")
```

Ця функція створює та виконує запити до бази даних, такі як створення нод, створення зв'язків, виведення графа, видалення зв'язків та видалення нод.

### Використання з'єднання

Ініціалізуйте об'єкт `Neo4jConnection` та використовуйте його для виклику функції `create_and_query_data`:

```python
neo4j_connection = Neo4jConnection(uri, username, password)
with neo4j_connection.connect() as driver:
    # Виклик функції create_and_query_data в рамках транзакції
    driver.session().write_transaction(create_and_query_data)
```

### Закриття з'єднання
Закриває з'єднання після завершення роботи:

```python
neo4j_connection.close()
```

