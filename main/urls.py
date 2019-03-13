from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
   
    path("products/",views.products,name="products"),
    # path("register/",views.homepage,name="homepage"),
    # path("manf/",views.homepage,name="homepage"),
    path("home/",views.homepage,name="upload"),
    path("upload/",views.upload,name="upload"),
    path("manf/",views.manf,name="upload"),
]