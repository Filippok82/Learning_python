# _________________Анонимная функция lambda__________________

# def f(x):
#     x**2

# g=f
# print(f(2))
# print(g(2))

# __________________________________________________

# def f(x):
#     return x**2


# print(f(2))

# ____________________________________________________

# def f(x):
#     return x**2

# g=f
# print(type(g))
# print(type(f))

# print(f(4))
# print(g(4))


# _________________________________________________________

# def calc(x):
#     return x+10
# print(calc(10))


# def calc1(x):
#     return x*10
# print(calc1(10))


# def math(op,x):
#     print(op(x))
# math(calc1, 10)
# math(calc, 10)


# ___________________________________________

# def sum(x,y):
#     return x+y

# f=sum
# def mylt(x,y):
#     return x*y
# def calc(op,a,b):
#     print(op(a,b))
#     # return op,a,b

# calc(f, 4, 5)

# _______________________________________________________


# def sum(x,y):
#     return x+y

# sum=lambda x,y:x+y+22

# def mylt(x,y):
#     return x*y

# def calc(op,a,b):
#     print(op(a,b))
#     # return op,a,b

# calc(sum, 4, 5)

# ___________________________________________________

# def mylt(x,y):
#     return x*y

# def calc(op,a,b):
#     print(op(a,b))
#     # return op,a,b

# calc(lambda x,y:x+y+22, 4, 5)

# ___________________________________ПРИМЕРЫ___________
# sum = lambda x: x+10
# mult = lambda x: x**2
# print(sum(mult(2)))


# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# print(sum1(mult2(2)))

# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# print(sum4(mult2(2)))


# _____________________List Comprhension_______________________


# list=[]

# for i in range(1,101):
#     if(i%2==0):
#         list.append(i)
# print(list)


# ________________________________________

# list=[(i,i) for i in range(1,21) if i%2==0]  # вывод картежей четных чисел


# print(list)


# ___________________________________________________________

# def f(x):
#     return x**3
# list=[(i,f(i)) for i in range(1,21) if i%2==0]  # использование метода сначала происходит выборка четных чисел, затем кубы в картеже


# print(list)

# ____________________________Задача с использованием lambda  функций_____________________________

# # path='C:/Users/Ирина/python/Learn_Python/Lecture/file.txt' # путь к файлу
# f = open('file.txt', 'r') #связываем файловую переменную c файлом на диске
# data = f.read() + ' ' # считываем все что  в строчке и исскуственно дабовляю пробел
# f.close()   # закрываем
# numbers = [] # создаем пустой список
# while data != '':# проходим по всей строке проверяем "пока моя строка не пустая"
#  space_pos = data.index(' ')# находим первую позицию пробела
#  numbers.append(int(data[:space_pos]))   # взять от первого символа до позиции первого пробела, превратить в число и добавить в список чисел
#  data = data[space_pos+1:]# обновить строку с учетом что добавили использовать не нужно

# out = []#создаем новый список
# for e in numbers:#пробегаем по исходному списку
#  if not e % 2:# проверяем условия
#     out.append((e,e **2))#добавим в новый список картеж
# print(out)#


# _______________________________________улучшаем код решения этой задачи_______________

# def select(f, col): # Принимает функцию  и набор данных
#      return [f(x) for x in col] # формирум новый список и сразу его возвращаем
# def where(f, col):                 # еще одна функция с набором данных
#  return [x for x in col if f(x)]  # возвращает список
# data = '1 2 3 5 8 15 23 38'.split() # создаем набор строк
# res = select(int, data)             # сохраняем результат в список res преобразум строк (split) в число в качестве набора данных будет data


# res = where(lambda x: not x % 2, res) # в res положим результат работы функции where
# res = select(lambda x: (x, x**2), res) #
# print(res)


# ________________________________Функция map_________________________________

# li = [x for x in range(1, 20)]
# li =list( map(lambda x:x+10,li))
# print(li)

# ________________________________________________________________________

# data= list( map(int,input().split())) # перевод вводимых данных из строки в число

# print(data)

# ____________________________________________________________________________________

# data= list(map(int,'1 31 98'.split()))
# for e in data:
#     print (e)

# print('--------')
# for e in data:
#     print (e)

# ________________________________________________________________________________


# def where (f,col):
#   return [x for x in col if f(x)]  # 
# data = '1 2 3 5 8 15 23 38'.split() # 
# res = map(int, data)             #


# res = where(lambda x: not x % 2, res) #
# res = list(map(lambda x: (x, x**2), res)) #
# print(res)
 

#______________________________Функция filter____________________________

# data = [ x for x in range((10))]

# res = list(filter(lambda x: not x%2, data))
# print(res)

#_________________________________________________________________


# data = '1 2 3 5 8 15 23 38'.split() # 
# res = map(int, data)             #


# res = filter(lambda x: not x % 2, res) #
# res = list(map(lambda x: (x, x**2), res)) #
# print(res)
 
#______________________Функция zip__________________________________

# users=['user1','user2','user3','user4', 'user5',]

# ids=[4,5,9,8,7]

# sal=[123,258,897]
# data=list(zip(users,ids,sal))


# print(data)

#_______________________Функция enumerate_____________________

users=['user1','user2','user3','user4', 'user5',]

data=list(enumerate(users))


print(data)