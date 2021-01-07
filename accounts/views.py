from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']

        # print(password)

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('login succesfull')
            return redirect("/")
        else:
            messages.info(request, 'Username or Password not correct')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist')
                print('Username already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email id already in use')
                print('Email id already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password1, email=email)
                user.save()
                messages.info(request, 'user created')
                print('user created')
                return render(request, 'login.html')
        else:
            messages.info(request, 'Passwords Does not Match')
        return redirect('register')
    else:
        return render(request,'register.html')


# {% load socialaccount %}

# def google(request):
#     return render(request, "provider_login_url 'google'")