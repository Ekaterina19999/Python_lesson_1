from company_api import CompanyApi  # Добавили импорт API
from company_table import CompanyTable

# Выносим настройки подключения наверх, чтобы они были доступны всем тестам
db_string = "postgresql://qa:skyqa@139.100.217.192:5432/x_clients"
api_url = "http://139.100.217.192:8000"

# Создаем общие объекты-помощники
db = CompanyTable(db_string)
api = CompanyApi(api_url)


# 1. Ваш первый тест (проверка, что база не пустая)
def test_company_list_is_not_empty():
    companies = db.get_companies()  # Используем созданный выше объект db
    assert len(companies) > 0


# 2. Ваш новый тест (создание через API + удаление через БД)
def test_add_new():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    # Делаем проверки, пока данные точно есть в списках бэкенда
    assert len_after - len_before == 1

    found = False
    for company in body:
        if company["id"] == new_id:
            found = True
            assert company["name"] == name
            assert company["description"] == descr
            break

    assert found

    # Выполняем очистку в самом конце, когда все ассерты успешно пройдены
    db.delete(new_id)

