#lists - СПИСКИ

# method append дополняет список какими либо элементами
# list1 = []
# list1.append('bitch')
# print(list1)
# print(len(list1))
# list1.append('hi')
# print(list1)
# print(len(list1))
# string = ' '.join(list1)
# print(string)
# list1.append(['gicci','flip'])
# print(list1)
# print(len(list1))


# func range создание списков каких то чисел

# list1 = list(range(1,50,3))
# print(list1)

# method isert получает два аргумента, первый индекс,второй это сам элемент
# cars = ['BMW','Ferrari','Maseratti']
# print(len(cars))
# print(cars)
# cars.insert(0,'Bugatti')
# print(cars)
# cars.insert(0, 96)
# print(cars)
# list1 = list(range(1,6))
# cars.insert(1,list1)
# print(cars)
# print(len(cars))

# method remove удаляет элемент по названию
# laptops = ['macbook','asus','acer','hp','acer']
# print('before',laptops)
# laptops.remove('acer')
# print('after',laptops)


# method pop удаляет и возварщает элемент
#
# prog = ['c','python','js','go','java']
# print('before',prog)
# last_elem = prog.pop()
# print('after',prog)
# print(last_elem)
# last_elem = prog.pop(0)
# print(last_elem)

# method index возварщает индекс элемента(нумерация)
#
# movies = ['star wars','джентльмены','why him?','godfather','1+1']
# print(movies.index('1+1'))
# mun_in_list = movies.index('1+1')
# print(mun_in_list)
# print(mun_in_list + mun_in_list)


# method count считает количество элементов
#
# list1 = ['apple','banana','pineapple','coconut','apple']
# print(list1.count('apple'))
# str = 'gucci flip flop'
# print(str.count('l'))
# new_list = list(str)
# print(new_list)
# splitted = str.split()
# print(splitted)

# method reverse разворачивает список в обратную сторону(только к списку)
#
# num = [1,2,3,4,5,6]
# print(num)
# num.reverse()
# print(num)

# method sort сортирует элементы в списке по ключу
#
# num = [5,2,1,4,3]
# print(num)
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
# num2 = ['Asan','Uson','Hasan','Ahmed','Vazgen']
# num2.sort(key=len)
# print(num2)
# num2.sort(key=len, reverse=True)
# print(num2)

# method copy копирует список
#
# list1 = ['apple','banana','pineapple','coconut','apple']
# new_list = list1.copy()
#
# new_list.append('applepen')
# print(new_list)
# print(list1)

# method extend расширяет список другим списком(складывает)
#
# num1 = [1,2,3]
# num2 = [4,5,6,7]
# num3 = num1 + num2
# print(num3)
# num1.extend(num2)
# print(num1)
#
# x = 10
# x += 10 #x=x+10
# print(x)

# method clear очищает список
#
# num1 = [1, 2, 3, 4, 5, 6, 7]
# print(num1)
# num1.clear()
# print(num1)

# num = [1, 2, 3, 4, 5, 6, 7]
# print(num[3])
# print(num[0:3])
# print(num[::-1])


# tuple = (1, 2) #кортеж(схожий со списком,круглая скобка и нельзя изменять)
# type(tuple)