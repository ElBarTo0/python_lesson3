#dictionary словарь
# dict_wtih_pirs = {'ключь':'значение','ключь2':'знаение2'}
# dict1 = {3: 1, 3.4: 2, 3: 2}
# print(dict1)

#method fromkeys создает новый словарь из переданных ему ключей
#
# names = {'name1': 'Ahmet', 'name': 'Vazgen'}
# print(names['name1'])

# dictionary = dict.fromkeys(['key1', 'key2'])
# print(dictionary)
# dictionary2 = dict.fromkeys(['key1', 'key2'], ['val1', 'val2'])
# print(dictionary2)

# извлечение данных словаря
# test = {'name': 'Ahmet', 'lastname': 'snow'}
# print(test['name'])
# print(test['lastname'])
#
# dict1 = {1:5, 2:8, 3:4}
# dict1[4] = 10 + 5
# print(dict1)
# dict1['bitch'] = 'boss'
# dict1['key'] = [1,2,3,4]
# dict1['key1'] = {1:1}

# dictionary = {}
# dictionary[1] = 1
# print(dictionary)
# dictionary['dictionary2'] = {2:2}
# print(dictionary)
# dictionary['dictionary2'][3] = 3
# print(dictionary)
# print(dictionary['dictionary2'][3])


#method get получает по ключу значения
#
# cars = {'chaser':'110', 'mark':'100', 'cresta':'tourerV'}
# print(cars.get('mark'))
# print(cars['cresta'])

#method keys выводит все ключи
#
# cars = {'chaser':'110', 'mark':'100', 'cresta':'tourerV'}
# print(cars.keys())
# cars_list = cars.keys()
# print(cars_list)
# print(len(cars))
# japan = cars.get('mark')
# print(japan)


#method values выводит все значения
#
# cars = {'chaser':'110', 'mark':'100', 'cresta':'tourerV'}
# print(cars.values())
# print(type(cars.values()))

#method pop удаляет по ключу и возвращает значение, нужно указывать ключь в скобках
#
# dict1 = {'first': '1st', 'second': '2nd', 'third': '3rd'}
# print(dict1)
# firs = dict1.pop('first')
# print(dict1)
# print(firs)

#method popitem вырезает последнюю пару ключь и значение, но возвращает только занчение
#
# cars = {'chaser':'110', 'mark':'100', 'cresta':'tourerV'}
# deleted = cars.popitem()
# print(deleted)
# print(cars)

# method update объединяет словари в 1
 #
# laptops = {'huyovo':'yoga', 'pontbook': 'pro', 'anus': 'zephyrus'}
# laptops2 = {'dell': 'allienware'}
# lap = {'ska':'blyat'}
# print(laptops)
# laptops.update(laptops2)
# print(laptops)
# laptops.update(lap)
# print(laptops)

#method setdefault сохраняет значение по ключу
#
# dict1 = {'key': 1, 'key1': 2, 'key3': 3}
# dict2 = dict1.setdefault('key1')
# print(dict2)
# new = dict1['key1']
# print(new)
# new1 = dict1.get('key1')
# print(new1)

# capitals = dict(Russia = 'Moscow', Kg = 'Bishkek', GB = 'London') #способ создания словаря
# print(capitals)


#####  Set ---> Множества

# set1 = [1,2,3,4,5,4,3,2,1,3,4,5,7]
# print(set1)
# set1 = set(set1)
# print(set1)

# set1 = {1,2}
# print(set1)
# print(type(set1))

#method add добавляет значение во множество
#
# set1 = {1,2,3}
# print(set1)
# set1.add(4)
# print(set1)

#method remove удаляет элемент
# set1 = {2,4,5,2,3,1}
# print(set1)
# set1.remove(2)
# print(set1)

# method discard удаляет элемент
#
# set1 = {2,4,5,2,3,1}
# set1.discard(1)
# print(set1)


#method pop вырезает элемент

set1 = {1,2,3,4,5,6,7,8,9,0}
print(set1.pop())