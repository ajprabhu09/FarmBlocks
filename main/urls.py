from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
   
    # path("products/",views.homepage,name="homepage"),
    # path("register/",views.homepage,name="homepage"),
    # path("manf/",views.homepage,name="homepage"),
    path("upload/",views.upload,name="upload")
]