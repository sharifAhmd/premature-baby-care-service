from django.urls import path
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    path('', login , {'template_name':'loginandregister/loginandregister.html'}),
    path('profile/', views.profile),
]
