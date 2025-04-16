from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your name'}), min_length=2, max_length=10)
    age = forms.IntegerField(widget=forms.Textarea(attrs={'placeholder': 'Your age'}), min_value=1, max_value=100)
    promo = forms.BooleanField(label='Do you are agree to receive promo?', required=False)
