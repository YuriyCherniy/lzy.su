from django import forms


class UrlCreateForm(forms.Form):
    long_url = forms.URLField(max_length=2048)
