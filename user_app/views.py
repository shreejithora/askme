from django.shortcuts import render, redirect
from django.http import HttpResponse
from user_app.models import UserModel


# Create your views here.

def loginauth(request):
    if request.method == "POST":
        e = request.POST.get('email')
        p = request.POST.get('pass')
        users = UserModel.objects.filter(email=e, password=p)
        if(users.count() > 0):
            for user in users:
                request.session['email'] = user.email
                request.session['id'] = user.id
                request.session['name'] = user.name
                return redirect('qna:read')
        else:
            return HttpResponse('Wrong Credentials')
    else:
        return render(request, 'login.html')

def logout(request):
    request.session.flush()
    return redirect('user:login')

    # return HttpResponse('logged out')