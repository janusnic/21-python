# -*- coding:utf-8 -*-

def fetcher(obj, index):
	return obj[index]

x = 'spam'
fetcher(x, 3)           # Like x[3] 'm'

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print 'got exception'
    print 'continuing'

catcher() # got exception continuing
