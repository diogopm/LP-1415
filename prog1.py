# coding=utf-8
import math
import random

print type(1), type(3.4), type((3 + 3j) + 2)

print type("treta"), type(True and False)

a = '1'
b = "Uma"

print type(a), type(b)
print type([1, 2, 3, [2, 3]]), type((1, 2, 3))

"""
class Teste:
    def __init__(self):
        pass


print type(Teste)

obj = Teste()
print type(obj)
"""

def func():
    return 3

    print type(func)


print type(range(0, 10))
print type(xrange(0, 10))
print type(a > 10 if 10 else 2)
print type(a) == type("string") if "uma string" else "nao sei"

print type(3j + 1.2)


def randomlist():
    randlist = []
    for i in range(0, 100):
        randlist.append(random.randint(0, 200))

    print randlist

    return randlist


def var(lista):
    """

    :rtype : object
    """
    avg = sum(lista) / len(lista)
    print type(avg)
    a = 0
    print 'média: ' + str(avg)
    #print 'somatório: ' + str(sum(lista))
    print 'tamanho da lista: ' + str(len(lista))

    for x in lista:
        a += (x - avg)**2

    var = a / (len(lista))
    return var


print 'Variância: ' + str(var(randomlist()))

lista = ['a', 'b', 'c']
# lista = [1,2,3,4,5]
string_b = reduce(lambda x, y: x + y, lista)

print string_b
