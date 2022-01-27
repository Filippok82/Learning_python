#print('Ввведите а')
#a=input()
#print ('Введите b')
#b=input()
#c=a+b
#print(a,b) #Вывод вариант 1
#print ('{}  {}'.format(a,b)) #Вывод вариант 2
#print (a,'+',b,'=',c) # Вывод вариант 3 (слияние числа если a=10 b=20 c=1020)

#------------------------------------------------------------------------------
#print('Ввведите а')
#a=int(input())
#print ('Введите b')
#b=float(input())
#c=a+b
#print ('{} + {} = {}'.format(a,b,c))
#print (a,'+',b,'=',c)

#___________________________________________________________________________________

#s= 'Вывод строки'
# print(s)

#________________________________________________________________________________

#list=[5,8,9,7,6,5]  # массив или списки
#print(list)

#__________________________________________________________________________________

#a=+569 # унарный плюс
#b=-698 # унарный минус
#c=a+b
#print(c);

#________________________________________________________________________________

#a=68
#b=5
#c=a/b # деление  // - деление в целых числах
#print(c);

#_________________________________________________________________________________

#a = 2.3655
#b = 5
#c = round(a*b,2) # функция округления где 2 сколько чисел после округления
#print(c);


#__________________Логические операции______________________________

#a=5<10
#print(a)
  
#a=5<9<7>2 # можно использовать тройное четверное сравнение
#print(a)


#a=1<6 or 7<3
#print(a)

#a=1<6 and 7<3
#print(a)

#________________________________________________

#f=[1,4,8,9,6]

#print(f)
#print(not 6 in f)


#f=[1,2,37,56]
#print (f)
#is_odd = not f[2]%2==0
#print(is_odd)


#  ________________Управляющие конструкции: if,if-else___________________

#print('Введите а:')
#a=int (input())
#print('Введите b:')
#b=int(input())
#ifa>b:
#    print('{} max'.format(a))
#else:
#    print('{} min'.format(b))    

#_____________________________________________________________________


""" username = input('Введите имя: ')
if username == 'Саша':
    print('Ура, это же Саша!')
elif username == 'Николай':
    print('Я так ждала Вас, Николай!')
elif username == 'Фокус':
    print('Фокус-покус)')
else:
    print('Привет, ', username)  """

#_____________Управляющая конструкция while_______________

""" number=45
inverted=0
while number!=0:
    inverted=inverted*10+(number%10)
    number//=10
print(inverted)     """

#________________конструкция while else___________________

""" number=45
inverted=0
while number!=0:
    inverted=inverted*10+(number%10)
    number//=10
    print((number))
else:
    print('Хватит')
    print('на сегодня')
print(inverted)        
 """

 #_________________Управляющие конструкции for___________________

""" list = [3,56,85,6,23,8]
for i in list:
    print(i**2)
 """

#____________________________________________________________________

""" r = range(6,22,2)
for i in r: # перечисляет числа от 6 до 22 (если добавить (6,22,2) двойку то выведутся через двойку)
    print(i)# также можно работать со строкой 
 """

 #_____________________Еще о строках________________________________

#text = 'малыш самый милый мальчик'


#print(len(text)) # 25
#print('милый' in text) # True
#print(text.isdigit()) # False
#print(text.islower()) # True
#print(text.replace('милый','МИЛЫЙ')) #
#for c in text:
#    print(c)
    

#help(text.isalnum)

#_______________________Срезы______________________________


""" text = 'собака самый лучший и близкий друг'
print(text[0])             # c
print(text[1])             # о
print(text[len(text)-1])   # г
print(text[-4])            # д
print(text[:])             # print(text) от первого до последнего
print(text[:5])            # собак
print(text[len(text)-2:])  # уг
print(text[2:9])           # бака са
print(text[7:-18])         # самый луч
print(text[0:len(text):6]) # с ийд
print(text[::6])           # с ийд
text = text[2:9] + text[-5] + text[:2] # .. """


#______________________Списки________________________________________

""" numbers = [1, 2, 3, 4, 5]      # [1, 2, 3, 4, 5]
print(numbers) 
ran=range(1,6)    
print(type(ran))                  
numbers = list(ran)
print(type(numbers))
print(numbers)                 # [1, 2, 3, 4, 5]
numbers[0] = 10
print(f'{len(numbers)} len')
print(numbers)                 # [10, 2, 3, 4, 5]
for i in numbers:
 i *= 2
 print(i)                      # [20, 4, 6, 8, 10]
print(numbers)                 # [10, 2, 3, 4, 5] """

#______________________________________________________________________

""" 
colors = ['red', 'green', 'blue']
for e in colors:
 print(e)                         # red green blue
for e in colors:
    print(e*2)                      # redred greengreen blueblue
colors.append('gray')            # добавить в конец
print(colors == ['red', 'green', 'blue', 'gray']) # True
colors.remove('red')              #del colors[0] # удалить элемент

del colors[0]
print(colors) """

#__________________Функции______________________________

def f(x):
 return x**2
def f(x):
 if x == 1:
    return 'Целое' 
 elif x == 2.3:
    return 23 
 else:
    return

arg=2.3
print(f(arg))   
print(type(f(arg)))   