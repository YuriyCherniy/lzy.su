from django.urls import path

from core.views import IndexView, TermsOfUseView

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('terms/', TermsOfUseView.as_view(), name='terms_of_use'),
]
