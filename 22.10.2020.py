##методы строк --strings

# method split
#tabnine
# text = 'Hello,World,Good,Morning'
# print(text.split())
#method isdigit проверяет все ли символы в строке цифры/true or False

# num = input('write num: ')
# print(num.isdigit())

# method isalpha проверяет является ли вся строка буквами

# text = input("write something: ")
# print(text.isalpha())


# method isalnum проверяет все ли символы в строке цифры и буквы

# text = input("write something: ")
# print(text.isalnum())

# method replace метод заменяет часть строки

# str = 'hello bitch!'
# print(str.replace('hello','hi'))
# print(str.replace('h','*',1))

# method isupper проверяет все ли символы в верхнем регистре

# text = input('write something: ')
# print(text.isupper())


# method islower проверяет все ли символы в нижнем регистре

# text = input('write something: ')
# print(text.islower())

# method isspace проверяет все ли символы пробелы,табы либо переводы строки

# text = input('write something: ')
# print(text.isspace())

# method istitle проверяет является ли строка заголовком

# txt = 'hi bitch'
# txt2 = 'Hi Bitch'
# print(txt.istitle())
# print(txt2.istitle())

# method lower() переводит буквы в нижний регистр

# txt = "Hi biITch"
#
# print(txt.lower())

# method upper переводит в верхний регистр

# str = 'hola muchacho'
# print(str.upper())


# method startswith проверяет начинается ли строка с определенных символов

# text = 'Hello miamigo'
# print(text.startswith('Hell'))

# method endswith проверяет заканчивается ли строка на какие либо символы

# check = 'something@gmail.com'
# print(check.endswith('.com'))


# method join склеивает строку из разных частей

# txt = 'hi bitch, surprise mothfk'
# text_splitted = txt.split()
# print(text_splitted)
# txt2 = ' '.join(text_splitted)
# print(txt2)

# method ord показывает нумерацию того или иного символа (таблица ASCII)

# print (ord('*'))

# method count считаетколичество символов переданных в скобках

# txt = 'Hi amigo'
# print(txt.count('i'))


# method strip,lstrip, rstrip удаляет пробелы в начале и в конце строки
# txt = '   hi   '
# print(txt.strip())
# print(txt.lstrip())
# print(txt.rstrip())

# method swapcase меняет регистр букв на противоположные

# txt = 'Hi Bitch'
# txt1 = 'konichiwa'
# print(txt.swapcase())
# print(txt1.swapcase())


# Срез строки

# text = ('write simething')
# print(text[::2])


# форматирование строк

# name = input('write your name: ')
# age = input('write your age: ')
# print('you are '+ name + '. And you at '+ age)
# print(f'you are {name}. And you at {age}.')

# print('hello, {}'.format(name))

# text = '''
#
# '''

# text = 'hello \nfill' #абзац
# print(text)
#
# text = 'hello \t fill' #tab



