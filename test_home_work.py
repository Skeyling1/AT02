import pytest
from home_work import vowels_count


# Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
def test_vowels():
    assert vowels_count("eiioaaue") == 8


@pytest.mark.parametrize("test_input, expected", [
    ("ghjdft", 0),# Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
    ("ewktyuoienyue", 7)# Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).
])
def test_vowels_count_check(test_input, expected):
    assert vowels_count(test_input) == expected


