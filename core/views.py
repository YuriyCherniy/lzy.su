from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('core/static/text.txt', 'r') as f:
            context['text'] = f.read()
        return context


class RobotsTxt(TemplateView):
    template_name = 'core/robots.txt'
    content_type = 'text/plain'


class TermsOfUseView(TemplateView):
    template_name = 'core/terms_of_use.html'