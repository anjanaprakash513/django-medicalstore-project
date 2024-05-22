from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.views.decorators.cache import cache_control


 
def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('retrieveproduct')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('retrieveproduct')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    # context = {
    #     'user': request.user
    # }

    # return render(request, 'signup.html')
    return redirect('login')