from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def hello(request):
    #Query data from model
    data = Post.objects.all()
    return render(request, 'index.html', {'posts':data})

def home(request):
    return render(request, 'home.html')

def register(request):
    return render(request, 'register.html')

def addUser(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']

    if password == repassword:
        if User.objects.filter(username = username).exists():
            print('This username is already.')
            return redirect('/register')
        elif User.objects.filter(email = email).exists():
            print('This E-mail is already.')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email,
                first_name = firstname,
                last_name = lastname,
            )
            user.save()
            return redirect('/')
    else:
        print('Your password is not relate.')
        return redirect('/register')

    