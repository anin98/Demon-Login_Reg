from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import CustomerUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.save()
            login(request,user)
            return redirect('home')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

