
import math
import random

print type(1), type(3.4), type((3+3j) + 2)

print type("treta"), type(True and False)

a = '1'
b = "Uma"

print type(a), type(b)
print type([1,2,3,[2,3]]), type((1,2,3))

class Teste:
	pass

print type(Teste)

obj = Teste()
print type(obj)

def func():
	return 3

	print type(func)

print type(range(0,10))
print type(xrange(0,10))
print type(a > 10 if 10 else 2)
print type(a) == type("string") if "uma string" else "nao sei"

print type(3j + 1.2)


def randomList():
	randomList = []
	for i in range (0, 100):
		randomList.append(random.randint(0, 200))

	print randomList

	return randomList



def var(l1):
	avg = sum(l1) / len(l1)
	a = 0

	print sum(l1)
	print len(l1)

	for x in l1:
		a += ((x - avg) * (x - avg))

	var = a / (len(l1) - 1)



	return var


print var(randomList())

lista = ['a','b','c']
#lista = [1,2,3,4,5]
string_b = reduce(lambda x,y: x+y, lista)

print string_b
