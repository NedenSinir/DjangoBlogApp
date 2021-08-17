
from django.contrib import admin
from django.urls import path,include
from article.views import *

urlpatterns = [
    path('dashboard/', dashboard,name="dashboard"),
    path('dashboard/addarticle', addarticle,name="addarticle"),
    path("readarticle/<int:id>",readarticle,name="readarticle"),
    path("dashboard/update/<int:id>",update,name="update"),
    path("dashboard/delete/<int:id>",delete,name="delete"),
    path("commet/<int:id>",commet,name="commet"),
    path("",article,name="article"),
]