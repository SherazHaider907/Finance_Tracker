from django.urls import path
from finance.views import RegisterView
urlpatterns = [
    path('register/',RegisterView.as_view(),name="register")
]
