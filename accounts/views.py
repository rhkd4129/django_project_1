from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def profile(request):
    pass
def sign_up(request):
    return render(request,'accounts/singup.html')
# Create your views here.
