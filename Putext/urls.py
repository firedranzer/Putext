from django.conf.urls import url
from django.urls import path
from django.contrib import admin

from home.views import home
from .views import GeneratePDF

urlpatterns = [
    url(
        regex = '^pdf/$',
        view = GeneratePDF.as_view(),
        name = 'pdfGenerator'
    ),
    url(
        regex = '^$',
        view = home.as_view(),
        name = 'home'
    ),
    path('admin/', admin.site.urls),
]
