from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^accueil/$', views.home),
    url(r'^accueil1/$',views.site),
]

