# -*- coding:utf-8 -*-

def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'



fetcher(x, 4)
# Traceback (most recent call last):
#  File "<stdin>", line 1, in ?
#  File "<stdin>", line 2, in fetcher
# IndexError: string index out of range



try:
    fetcher(x, 4)
except IndexError:
    print 'got exception' # got exception
