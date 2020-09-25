from os import name
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith("aaa"):
            raise forms.ValidationError("Email address is not valid, aaa")
        return email
