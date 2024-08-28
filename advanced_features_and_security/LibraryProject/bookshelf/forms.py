from django import forms

class ExampleForm(forms.Form):
    # Add form fields here
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea) 