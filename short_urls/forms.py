from django import forms

from short_urls.validators import ForbiddenDomainValidator


class UrlCreateForm(forms.Form):
    long_url = forms.CharField(max_length=2048, validators=[ForbiddenDomainValidator()])
