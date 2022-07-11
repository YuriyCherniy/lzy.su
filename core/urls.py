from django.urls import path

from core.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index-view')
]
