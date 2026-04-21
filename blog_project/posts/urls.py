






from django.urls import path
from . import views 

app_name = "posts" 

urlpatterns = [
    path('', views.list, name="list"),
    path('new', views.post_new, name="post-new"),
]
