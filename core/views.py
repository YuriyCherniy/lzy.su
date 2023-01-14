from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'


class RobotsTxt(TemplateView):
    template_name = 'core/robots.txt'
    content_type = 'text/plain'


class TermsOfUseView(TemplateView):
    template_name = 'core/terms_of_use.html'