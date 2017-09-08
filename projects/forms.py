from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email_address = forms.EmailField(label='Your email', max_length=100)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
