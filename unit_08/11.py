# -*- coding:utf-8 -*-

print '-' * 30, '\nEXCEPTION RAISED AND CAUGHT'
try:
    x = 'spam'[99]
except IndexError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'

print '-' * 30, '\nNO EXCEPTION RAISED'
try:
    x = 'spam'[3]
except IndexError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'

print '-' * 30, '\nNO EXCEPTION RAISED, ELSE RUN'
try:
    x = 'spam'[3]
except IndexError:
    print 'except run'
else:
    print 'else run'
finally:
    print 'finally run'
print 'after run'


print '-' * 30, '\nEXCEPTION ZeroDivisionError'
try:
    x = 1 / 0
except ZeroDivisionError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'


print '-' * 30, '\nEXCEPTION RAISED BUT NOT CAUGHT'
try:
    x = 1 / 0
except IndexError:
    print 'except run'
finally:
    print 'finally run'
print 'after run'
