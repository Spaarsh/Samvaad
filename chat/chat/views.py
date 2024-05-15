from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect('/rooms/')
    else:
        return redirect('/accounts/login/')