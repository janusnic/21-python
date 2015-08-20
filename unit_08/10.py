# -*- coding:utf-8 -*-

# функция в Python'e может быть определена… внутри другой функции!

def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="да"):
        return word.lower()+"...";
    # ... и сразу же её использовать!
    print whisper()

# Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем
# и вызывается функция "whisper".

talk() # выведет: "да..."

# Но вне функции "talk" НЕ существует никакой функции "whisper":

try:
    print whisper()
except NameError, e:
    print e
    #выведет : "name 'whisper' is not defined"
