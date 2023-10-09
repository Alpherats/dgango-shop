from django.shortcuts import render
from .forms import UserForm


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            age = form.cleaned_data['age']
    else:
        form = UserForm()
    return render(request, 'lection4_app/user_form.html', {'form': form})
