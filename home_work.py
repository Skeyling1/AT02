#Напишите функцию, которая считает количество гласных в строке, и создайте тесты для этой функции.
# Проверьте, что функция правильно считает гласные в строке, содержащей только гласные.
# Проверьте, что функция возвращает 0 для строки, не содержащей гласных.
# Проверьте, что функция правильно считает гласные в смешанных строках (включая прописные и строчные буквы).

def vowels_count(string):
    list(string)
    vowels = ['a', 'e', 'u', 'i', 'o']
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count