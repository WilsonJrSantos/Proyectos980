from . import views
from django.urls import path

from apps.login.views import *

urlpatterns = [
    path("", LoginFormView2.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
]