from random import randint

from django.views import View
from django.db.models import F
from django.views.generic import TemplateView
from django.core.validators import URLValidator, ValidationError
from django.shortcuts import redirect, render, get_object_or_404

from short_urls.models import Url
from short_urls.hashids import Hashids


class UrlCreate(View):
    hashids = Hashids()
    validate_url = URLValidator()

    def get(self, request, **kwargs):
        url = kwargs.get('url', '')
        try:
            self.validate_url(url)
            short_url = self.hashids.encode(Url.objects.last().pk + 1)
            url_obj = Url.objects.create(
                long_url=url,
                short_url=short_url,
                password=randint(10000, 99999)
            )
        except ValidationError:
            return render(request, 'short_urls/url_create_error.html')
        return render(request, 'short_urls/url_create.html', {'url_obj': url_obj})


class UrlDelete(View):
    def get(self, request, **kwargs):
        password = kwargs.get('password')
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)

        if url_obj.password == password:
            url_obj.delete()
            return render(request, 'short_urls/url_delete.html')
        return render(request, 'short_urls/url_delete_error.html')


class UrlOpen(View):
    def get(self, request, **kwargs):
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)
        url_obj.click = F('click') + 1
        url_obj.save()
        return redirect(url_obj.long_url)


class UrlInformation(TemplateView):
    template_name = 'short_urls/url_information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)
        context.update({
            'url_click': url_obj.click,
            'url_created': url_obj.created,
            'long_url': url_obj.long_url
        })
        return context
