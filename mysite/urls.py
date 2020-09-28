from django.contrib import admin
from blog import views

from django.urls import path,include
urlpatterns = [


    path('blog/', include('blog.urls')),
    
]
