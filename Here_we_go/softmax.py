import numpy as np

def softmax(text_latents, image_latents):  #Собственно функция софтмакса, на вход две матрицы
    x = np.dot(text_latents, image_latents.T) #Перемножение матриц, матрица классов транспонируется
    e_x = np.exp(x) #Все значения x перемноженной матрицы переводятся в число е в степени х
    for j in range(x.shape[0]): #Итерация в число строк матрицы
        e_xs = 0    # первоначальная сумма всех значений в строке (на нее делим по формуле софтмакса)
        for i in range(x.shape[1]): #Итерация в число значений в строке (вообщем то тут всегда в нашем примере, но для гибоксти x.shape[1])
            e_xs += e_x[j][i] #собираем сумму значений в строке
        e_x[j]=e_x[j]/e_xs # элементы j-й строки перемноженной матрицы делятся на сумму элеметов этой строки 
    return (np.round(e_x, 4)) # на выходе получаем матрицу округленную до 4 знаков после запятой

def creatematrix(string): #это функция создания матрицы, но она нужна только ручного ввода с консоли, она тут не применяется, но я решил оставить
    matrix = []
    while string != '':
        if string == ['']:
            break
        else:
            for i in range(len(string)):
                string[i] = float(string[i])
            matrix.append(string)
            string = input().split(' ')
    return matrix

f = open('input.txt') # читаем текстовый файл
matrix = [line.replace("\n", "").split() for line in f] #создаем одну большую матрицу, куда включены сразу две нужные нам
matrix1 = [] #подготовливаем первую
matrix2 = [] #вторую
for i in matrix: #для всех строк в исходной большой матрце
    if i == []: #дело в том, что в текстовом документе для разделения матриц используется пустая строка, которая в нашей матрице записана
                #записана как пустой массив. Если он встерчается - значит мы прекращаем строить первую матрцу и прерываем цикл
        lenght = len(matrix1)   #Нужно зафиксировать, сколько элементов исходной матрицы было проитерировано
        break
    matrix1.append(i) #добавляем строку исходной матрицы в первую матрицу
for j in range(len(matrix) - lenght): #итерация по всей оставшейся длине исходной матрицы
    if j==0: #нулевой жлемент матрицы - пустая строка, скипаем
        continue
    else:
        matrix2.append(matrix[lenght + j]) #создаем вторую матрицу из исходной
matrix1 = np.array(matrix1, dtype=np.float32) #переводим в нумпай
matrix2 = np.array(matrix2, dtype=np.float32) #переводим в нумпай
res = softmax(matrix1, matrix2) #применяем софтмакс
f = open("output.txt", "w") #создаем новый файл

with open("output.txt", "w") as f: #редактируем этот новый файл
    for line in res: #для каждой стркои в матрице
        for elem in line: #для каждого элемента в строке
            f.write(str(elem)+' ') #вставляем этот элемент плюс пробел в наш текстовый output.txt
        f.write('\n') #после того, как стркоа закончена - переводим запись на новую строку



