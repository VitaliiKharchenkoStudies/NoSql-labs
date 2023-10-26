# Лабораторна робота 9 Харченко Віталій ІКМ-223Б

### Кожна цифра після якої йде шматочок команди або запиту символізує собою завдання лабораторної роботи з відповідним номером
1. Створення таблиці `department_table` з ключем `(department, email)`:

```cql
CREATE TABLE IF NOT EXISTS my_keyspace.department_table (
    department text,
    email text,
    name text,
    PRIMARY KEY (department, email)
);
```

2. Вставка записів:

```cql
-- Вставка запису 1
INSERT INTO my_keyspace.department_table (department, email, name) VALUES ('1', 'mail1@gmail.com', 'John');

-- Вставка запису 2
INSERT INTO my_keyspace.department_table (department, email, name) VALUES ('1', 'mail2@gmail.com', 'Igor');

-- Вставка запису 3
INSERT INTO my_keyspace.department_table (department, email, name) VALUES ('2', 'mail3@gmail.com', 'Andrew');
```

3. Вибірка запису, де `department = '1'` та `email = 'mail2@gmail.com'`:

```cql
SELECT * FROM my_keyspace.department_table WHERE department = '1' AND email = 'mail2@gmail.com';
```
   Результат:
   ```
   department | email           | name
  ------------+-----------------+------
            1 | mail2@gmail.com | Igor

   (1 rows)
   ```

4. Створення індексу `department_table_name_idx` для колонки `name`:

```cql
CREATE INDEX IF NOT EXISTS department_table_name_idx ON my_keyspace.department_table (name);
```

5. Вибірка запису, де `name = 'John'`:

```cql
SELECT * FROM my_keyspace.department_table WHERE name = 'John';
```
   Результат:
   ```
   department | email           | name
  ------------+-----------------+------
            1 | mail1@gmail.com | John

   (1 rows)
   ```

6. Оновлення запису, змінюємо `name` на 'Dmytro', де `department = '1'` та `email = 'mail2@gmail.com'`:

```cql
UPDATE my_keyspace.department_table SET name = 'Dmytro' WHERE department = '1' AND email = 'mail2@gmail.com';
```

7. Видалення запису, де `department = '2'` та `email = 'mail3@gmail.com'`:

```cql
DELETE FROM my_keyspace.department_table WHERE department = '2' AND email = 'mail3@gmail.com';
```

8. Вибірка всіх записів з таблиці:

```cql
SELECT * FROM my_keyspace.department_table;
```
   Результат:
   ```
   department | email           | name
  ------------+-----------------+--------
            1 | mail1@gmail.com |   John
            1 | mail2@gmail.com | Dmytro

   (2 rows)
   ```
![Завдання](https://media.discordapp.net/attachments/917547349864230912/1167239082754187314/image.png?ex=654d671b&is=653af21b&hm=901ffb0bb9173acddbccb7c44586f63d5f02a0c3184c70a43a83f6d6a50d64fa&=&width=1073&height=671)
