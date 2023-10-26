# Лабораторна робота 8 Харченко Віталій ІКМ-223Б

### Кожна цифра після якої йде шматочок команди або запиту символізує собою завдання лабораторної роботи з відповідним номером

1. `docker pull cassandra:4.1`
   - Ця команда використовує Docker для завантаження образу Cassandra версії 4.1 з Docker Hub. Образ Cassandra використовується для створення та управління Cassandra базою даних в контейнері Docker.

![Встановлення контейнеру](https://media.discordapp.net/attachments/917547349864230912/1167227939335712908/image.png?ex=654d5cba&is=653ae7ba&hm=ffe12fcfb1826b6f08095c60d211a9314090c516b5e229c2984403efa3909fd3&=&width=1073&height=671)

2. `cqlsh`
   - Після встановлення та запуску образу Cassandra, ви виконуєте команду `cqlsh`, що відкриває інтерактивний термінал для взаємодії з Cassandra за допомогою мови запитів CQL (Cassandra Query Language).

3. `create keyspace if not exists my_keyspace with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};`
   - Ця команда створює keyspace (простір ключів) з назвою "my_keyspace". Keyspace в Cassandra відповідає базі даних в інших системах керування базами даних. У цьому випадку використовується SimpleStrategy для розподілу даних з реплікацією на одину машину (replication_factor = 1).

4. `use my_keyspace;`
   - Ця команда встановлює keyspace "my_keyspace" як поточний, що означає, що всі наступні операції CQL будуть виконуватися у контексті цього keyspace.

5. `CREATE TABLE IF NOT EXISTS my_keyspace.my_table ( department text, email text, name text, PRIMARY KEY ((department), email) );`
   - Ця команда створює таблицю з назвою "my_table" у поточному keyspace "my_keyspace". Таблиця має три колонки: "department", "email" та "name". Колонка "department" використовується як частина складного первинного ключа, а "email" - як інша частина первинного ключа. Це означає, що комбінація "department" та "email" унікально і визначає унікальний рядок в таблиці.

6. `ALTER TABLE my_keyspace.my_table ADD phone text;`
   - Ця команда додає нову колонку з назвою "phone" до таблиці "my_table". Тепер таблиця має чотири колонки: "department", "email", "name" та "phone".

![Результат виконання](https://media.discordapp.net/attachments/917547349864230912/1167229694530310185/image.png?ex=654d5e5d&is=653ae95d&hm=ae114b62d5cc51df329f274fa44f52215ccfc4685dda0be50a64d19f0688e956&=&width=1073&height=671)