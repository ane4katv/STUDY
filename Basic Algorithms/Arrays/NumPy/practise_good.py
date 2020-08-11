# Practise NumPy
# more here: https://server.179.ru/tasks/python/2022a/pgm20.2__NumPy.html#prob_C

import numpy as np

# A: Массив нулей
def create_array(n):
    return np.zeros(n*2*n).reshape(n, 2*n)


# print(create_array(3))

# B: Числа в нулевой строке
def find_nums(n,m):
    a = np.zeros(n*m, dtype=np.int8).reshape(n,m)
    a[0] = np.arange(0, m)
    return a

# print(find_nums(3,5))

# C: Числа на диагонали
def build_array(n):
    a = np.zeros(n*n, dtype=np.int64).reshape(n,n)
    line = 0
    column = 0
    while column <= n-1:
        a[line, column] = column
        line += 1
        column += 1
    return a

# print(build_array(4))

# D: Сбитый прицел

def set_some(n, r, c):
    a = np.zeros(n*n, dtype=np.int64).reshape(n,n)
    a[r, :] = 1
    a[:, c] =1
    return a

# print(set_some(5,1,3))


# E: Почётные единицы
def even_lines(n):
    a = np.zeros(n*n, dtype=np.int64).reshape(n,n)
    i = 0
    while i < n:
        if i % 2 ==0:
            a[i,:] = 1
        i +=1
    return a


# print(even_lines(5))


# F: Решето
def change_some(n,m, r, c):
    a = np.ones((n, m), dtype = np.int8)
    a[r, :] = 0
    a[:, c] = 0
    return a

# print(change_some(5,11,3,4))


# G: Шахматы единиц
def checkboard(n):
    a = np.zeros((n, n), dtype=int)
    a[::2, ::2] = 1 #
    # a[1::2, 1::2] = 1

    return a

print(checkboard(5))
