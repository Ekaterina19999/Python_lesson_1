from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://qa:skyqa@139.100.217.192:5432/x_clients"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'app_users' in names

def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()
    
    assert len(rows) == 1
    assert rows[0]['name'] == "QA Студия 'ТестировщикЪ'"
    connection.close()

def test_select_1_row_with_two_filters():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE is_active = :is_active AND id >= :id")
    result = connection.execute(sql_statement, {"id": 65, "is_active": True})
    rows = result.mappings().all()
    
    assert len(rows) == 0
    connection.close()

def test_test_insert(): # Изменено имя, чтобы PyTest корректно подхватил функцию
    connection = db.connect()
    transaction = connection.begin()
    unique_name = "Skypro_Test_Company"

    try:
        insert_sql = text("INSERT INTO company(\"name\") VALUES (:new_name)")
        connection.execute(insert_sql, {"new_name": unique_name})
        
        select_sql = text("SELECT * FROM company WHERE name = :name")
        result = connection.execute(select_sql, {"name": unique_name})
        rows = result.mappings().all()
        
        assert len(rows) == 1
        assert rows[0]['name'] == unique_name

    finally:
        delete_sql = text("DELETE FROM company WHERE name = :name")
        connection.execute(delete_sql, {"name": unique_name})
        transaction.commit()
        connection.close()
        