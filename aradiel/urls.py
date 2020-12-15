
from django.conf.urls import include, url
from django.contrib import admin

from inicio import views


urlpatterns = [
    url(r'^$', views.inicio, name="inicio_redirect"),
    url(r'^ameliagallegos/', include('inicio.urls', namespace='inicio')),
    url(r'^academica/', include('academica.urls', namespace='academica')),
    url(r'^admin/', include(admin.site.urls)),
]
