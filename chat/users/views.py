from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('Logged in successfully')
        else:
            return HttpResponse('Invalid credentials', status=401)
    else:
        return HttpResponse('Invalid request', status=400)