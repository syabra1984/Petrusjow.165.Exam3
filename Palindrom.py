#Напишите функцию, которая проверяет: является ли слово палиндромом.
def palindrom(word):
    inverted_word = word[::-1]
    if inverted_word == word:
        print('Это палиндром')
    else:
        print('Это не палиндромом')
word = input('Введите слово: ')
palindrom(word)