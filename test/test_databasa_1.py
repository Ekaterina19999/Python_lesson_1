from sqlalchemy import create_engine, text

# Возвращаем старый рабочий IP-адрес
db_connection_string = "postgresql://qa:skyqa@139.100.217.192:5432/x_clients"
db = create_engine(db_connection_string, echo=True)

# Создаем и используем соединение
connection = db.connect()
select_all = text("SELECT * FROM company")
result = connection.execute(select_all)
rows = result.mappings().all()  # Получаем строки как словари

# Работа с результатами
# Выводим имя самой первой компании
print("Первая компания в списке:", rows[0]["name"])

print("\nСписок всех компаний:")
# Запускаем цикл (добавлен правильный отступ в 4 пробела)
for row in rows:
    print(row["id"], row["name"])

# Закрываем соединение
connection.close()