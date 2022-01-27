# _______________ФАЙЛЫ________________________________


# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2235\n')


# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write('\nLine13\n')
# data.write('Line12\n')
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#  print(line)
# data.close()


# exit()


# _______________________________Функции и модули_________________

# import lec_01
#                       # использование функции их файла Lec_01.py
# print (lec_01.f(1))

# ______________________________________________________________________
# import lec_01 as l   # использование тойже функции но с псевдонимом
# print(l.f(1))

# ___________________________________________________________________
# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ..    sympol- символ count - число


# ____________________________________________________________

# def new_string(symbol, count=3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!'))   # !
# print(new_string(4))   # 12


# __________________________________________________________

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# # print(conatenatio(1, 2, 3, 4)) # TypeError: ..

# ____________________________________________

# def concatenatio(*params):
#     res: int = 0
#     for item in params:
#         res += item
#     return res
# print(concatenatio(1, 2, 3, 4)) # 10

# ______________Рекурсия_____________


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
#  list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34

# _______________Кортежи________________________

# a=(3,4)
# print(a)
# print(a[0])

# _____________________________________________

# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# ____________________________________

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#  print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support

# _____________________________________________________

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue

# ___________Словари_______________


dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'down': '↓',
        'right': '→'
    }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться


# # for k in dictionary.keys(): # получение всех ключей
# #     print(k)

# for k in dictionary.values(): # получение только значение ключей
#     print(k)
# ___________________________________________________________


# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right:


# _____________________________Множества________________________________


# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# -_________________________________________________________

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}
# print(b)
# print(c)

# ____________________________________________________________


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# ____________________________________________________________

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))
# # {1, 21, 3, 13}
# print(c)
# print(u)
# print (i)
# print(dl)
# print(dr)
# print (q)


# __________________________________Неизменяемые множества__________________

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})


# _____________________________Списки_____________________________________

# list1 = [1, 2, 3, 4, 5]
# list2 = list1

# list1[1] = 123      # если меняем какой либо элемент в первом списке, то во втором тоже меняется
# list2[2]= 25        # если меняем какой либо элемент во второом спике в первом тоже меняется
# for e in list1:
#     print(e)

# print()


# for e in list2:
#     print(e)


#___________________________________________________

list1=[1,2,3,4,7]

print(list1)
print (list1.pop())
print(len(list1))
print(list1)
print (list1.pop())
print(len(list1))
print(list1)
print (list1.pop())
print(len(list1))
print (list1.insert(2,11))
print(list1)
print (list1.append(25))
print(list1)










