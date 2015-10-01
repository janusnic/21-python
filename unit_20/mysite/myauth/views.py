# -*- coding:utf-8 -*-
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

from myauth.forms import UserForm, UserProfileForm

def register(request):

    # boolean value
    # Установлено в False при инициализации. Изменим на True при успешной регистрации.
    registered = False

    # Если HTTP POST, обработаем форму.
    if request.method == 'POST':
        # Получаем информацию из форм.
        # Мы используем две формы UserForm и UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # Если обе формы прошли проверку...
        if user_form.is_valid() and profile_form.is_valid():
            # Сохраним данные пользователя из формы в database.
            user = user_form.save()

       # Хешируем пароль с помощью set_password method.

            user.set_password(user.password)
            user.save()

            # Пока пользователь настраивает свой профиль не выполнять commit=False.

            profile = profile_form.save(commit=False)
            profile.user = user

            # Юзер хочет картинку?
            # Если да, предоставим ему поле для ввода картинки.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Сохранить экземпляр модели UserProfile.
            profile.save()

            # Изменить переменную при успешной регистрации.
            registered = True

        # Ошибки?
        # Печать ошибок на terminal.
        else:
            print user_form.errors, profile_form.errors

    # Не HTTP POST, строим два эеземпляра ModelForm .
    # Эти формы пустые , предназначены для пользовательских вводов.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'myauth/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )


def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
            # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Blog account is disabled.")
        else:
       # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'myauth/login.html', {})

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/blog/')
