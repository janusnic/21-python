# -*- coding:utf-8 -*-

def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

try:
    fetcher(x, 3)
finally:
    print 'after fetch'


fetcher(x, 3)
print 'after fetch'

def after():
    try:
        fetcher(x, 3)
    finally:
        print 'after fetch'
    print 'after try?'

after()
