from django.views import View
from django.db.models import F
from django.views.generic import TemplateView
from django.core.validators import URLValidator, ValidationError
from django.shortcuts import redirect, render, get_object_or_404

from short_urls.models import Url
from short_urls.forms import UrlCreateForm
from short_urls.services import create_url_object


class UrlCreateSuccess(TemplateView):
    """
    View to redirect after successful creation a short url.
    Necessary for elegant URL scheme.
    """
    template_name = 'short_urls/url_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context_data = {k: self.request.session.get(k) for k in self.request.session.keys()}
        context.update(context_data)
        return context


class UrlCreate(View):
    """
    Create short url when user has typed command in browser's address bar
    """
    validate_url = URLValidator()

    def get(self, request, **kwargs):
        long_url = kwargs.get('url', '')
        try:
            self.validate_url(long_url)
            url_obj = create_url_object(long_url)

            # prepare dict to pass to UrlCreateSuccess for context data
            request.session.update({
                'long_url': url_obj.long_url,
                'short_url': url_obj.short_url,
                'password': url_obj.password
            })
            return redirect('url-create-success')
        except ValidationError:
            return render(request, 'short_urls/url_create_error.html')


class UrlCreateByForm(View):
    """
    Create short url the old way by HTML form
    """
    def post(self, request):
        form = UrlCreateForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')
            url_obj = create_url_object(long_url)

            # prepare dict to pass to UrlCreateSuccess for context data
            request.session.update({
                'long_url': url_obj.long_url,
                'short_url': url_obj.short_url,
                'password': url_obj.password
            })
            return redirect('url-create-success')

        with open('core/static/text.txt', 'r') as f:
            text = f.read()
        return render(request, 'core/index.html', {'form': form, 'text': text})


class UrlOpen(View):
    """
    Open short url and increment click counter
    """
    def get(self, request, **kwargs):
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)
        url_obj.click = F('click') + 1
        url_obj.save()
        return redirect(url_obj.long_url)


class UrlInformation(TemplateView):
    """
    Show short url's information when user has typed command in browser's address bar:
    https://lzy.su/<short_url_identifier>/<command>/<password>
    For example: https://lzy.su/Aq6/i/46754
    Command 'i' in the url means - Information
    """
    template_name = 'short_urls/url_information.html'

    def get(self, request, **kwargs):
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)
        if kwargs.get('password') == url_obj.password:
            self.url_obj = url_obj
            return super().get(request, kwargs)
        return render(request, 'short_urls/url_error.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'url_click': self.url_obj.click,
            'url_created': self.url_obj.created,
            'long_url': self.url_obj.long_url
        })
        return context


class UrlDelete(View):
    """
    Delete short url when user has typed command in browser's address bar:
    https://lzy.su/<short_url_identifier>/<command>/<password>
    For example: https://lzy.su/Aq6/d/46754
    Command 'd' in the url means - Delete
    """
    def get(self, request, **kwargs):
        password = kwargs.get('password')
        short_url = kwargs.get('short_url')
        url_obj = get_object_or_404(Url, short_url=short_url)

        if url_obj.password == password:
            url_obj.delete()
            return render(request, 'short_urls/url_delete.html')
        return render(request, 'short_urls/url_error.html')
