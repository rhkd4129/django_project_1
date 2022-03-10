from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm

def profile(request):
    pass


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm()
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')

    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form,})
# Create your views here.

