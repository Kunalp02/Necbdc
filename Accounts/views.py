from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from .models import Account



def loginUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')    
        else:
            messages.warning(request, 'Invalid login credentials')
    else:
        return render(request, 'Accounts/loginUser.html')


@csrf_exempt
def signupUser(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        paswd = request.POST['paswd']
        email = request.POST['email']
        username = email.split('@')[0]
        user = Account.objects.create_user(first_name=fname, last_name=lname, email=email, username=uname, password=paswd)
        return redirect('loginUser')
    
    return render(request, 'Accounts/signupUser.html')


def logOut(request):
    if request.user is not None:
        auth.logout(request)
        return redirect('index')