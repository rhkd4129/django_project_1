from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
def profile(request):
    pass


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = SignupForm()
    return render(request,'accounts/signup.html',{'form':form,})
# Create your views here.

