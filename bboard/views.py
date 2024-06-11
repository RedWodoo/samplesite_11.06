from django.shortcuts import render

from django.ccontrib import admin
from django.urls import path
from bboard.views import index
urlpaterns = [
    path('bboard/',index),
    path('admin/',admin.site.urls),
]