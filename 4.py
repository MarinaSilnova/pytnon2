#Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
number = int(input('Введите число: '))
list=[]
element = -number
while element<=number:
    list.append(element)
    element+=1
print(list)
list2 = list[len(list)-2:len(list)]
print(list2 + list[:len(list)-2])
