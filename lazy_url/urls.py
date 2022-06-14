"""lazy_url URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from short_urls.views import UrlOpen, UrlCreate, UrlInformation, UrlDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        r"^(?P<url>http[s]{0,1}://[[\]A-Za-zА-Яа-я0-9-._~:/?#@!$&'()*+,;=]{,2000})$",
        UrlCreate.as_view()
    ),
    path('<str:short_url>/', UrlOpen.as_view()),
    path('<str:short_url>/i', UrlInformation.as_view()),
    path('<str:short_url>/<int:password>', UrlDelete.as_view()),
]
