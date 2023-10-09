from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    mail = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=100)

