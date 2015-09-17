# -*- coding:utf-8 -*-
from django.shortcuts import render
import datetime

class MyStruct(object): 
    pass 


def index(request):
    # return render(request,'pages/index.html', {})
    c = MyStruct()
    c.company = 'Cool Star' 
    c.title = 'Drunk, fix later' 
    c.author_name = 'Jhon Smith' 
    c.pub_date = datetime.datetime.now()
    c.exerpt  = 'I dedicate all this code, all my work, to my wife, Darlene, who will have to support me and our three children and the dog once it gets released into the public.'
    c.article_list = [{'title':'Title1','text':'text1'},{'title':'Title2','text':'text2'},{'title':'Title3','text':'text3'}]
    c.message = "When I wrote this, only God and I understood what I was doing. Now, God only knows"
    c.text = 'Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ text|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.'
    return render(request, 'home/index.html',  c.__dict__)

def about(request):
    mydict = {'title': 'Over and over I keep going over the world we knew','template_name':'partials/head.html'}
    return render(request,'home/about.html', mydict)

def news(request):
    
    c = MyStruct()
    c.company = 'Cool Star' 
    c.title = 'Drunk, fix later' 
    c.pub_date = datetime.datetime.now()
    c.article_list = [{'title':'Title1','text':'text1','author_name':'Jhon Smith'},{'title':'Title2','text':'text2','author_name':'Mary Ann'},{'title':'Title3','text':'text3','author_name':'Jhon Doo'}]
        
    return render(request, 'home/news.html',  c.__dict__)