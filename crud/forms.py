from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    age = forms.IntegerField(widget=forms.Textarea(attrs={'placeholder': 'Your age'}))

    class Meta:
        model = Person
        fields = ('name', 'age')
