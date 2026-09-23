from string_utils import StringUtils

# Создаем объект класса перед тестами
utils = StringUtils()


# ================= ТЕСТЫ ДЛЯ МЕТОДА capitalize =================

def test_capitalize_positive_word():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_positive_already_capital():
    assert utils.capitalize("Skypro") == "Skypro"


def test_capitalize_positive_with_numbers():
    assert utils.capitalize("123sky") == "123sky"


def test_capitalize_negative_empty():
    assert utils.capitalize("") == ""


def test_capitalize_negative_whitespace():
    assert utils.capitalize(" ") == " "


# ================= ТЕСТЫ ДЛЯ МЕТОДА trim =================

def test_trim_positive_with_spaces():
    assert utils.trim("   skypro") == "skypro"


def test_trim_positive_no_spaces():
    assert utils.trim("skypro") == "skypro"


def test_trim_positive_spaces_in_middle():
    assert utils.trim("sky pro   ") == "sky pro   "


def test_trim_negative_empty():
    assert utils.trim("") == ""


def test_trim_negative_only_spaces():
    assert utils.trim("   ") == ""


# ================= ТЕСТЫ ДЛЯ МЕТОДА contains =================

def test_contains_positive_symbol_exists():
    assert utils.contains("SkyPro", "S") is True


def test_contains_positive_symbol_not_exists():
    assert utils.contains("SkyPro", "U") is False


def test_contains_negative_empty_string():
    assert utils.contains("", "S") is False


def test_contains_negative_empty_symbol():
    assert utils.contains("SkyPro", "") is True


def test_contains_negative_case_sensitive():
    assert utils.contains("SkyPro", "s") is False


# ================= ТЕСТЫ ДЛЯ МЕТОДА delete_symbol =================

def test_delete_symbol_positive_remove_one_letter():
    """Удаление одного символа из строки"""
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_positive_remove_substring():
    """Удаление целой подстроки из строки"""
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_positive_not_found():
    """Попытка удалить символ, которого нет в строке"""
    assert utils.delete_symbol("SkyPro", "x") == "SkyPro"


def test_delete_symbol_negative_empty_string():
    """Попытка удалить символ из пустой строки"""
    assert utils.delete_symbol("", "k") == ""


def test_delete_symbol_negative_empty_symbol():
    """Попытка удалить пустой символ из строки"""
    assert utils.delete_symbol("SkyPro", "") == "SkyPro"
