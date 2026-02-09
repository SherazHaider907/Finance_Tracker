from django.urls import path
from finance.views import RegisterView,DashboardView
urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('',DashboardView.as_view(),name="dashboard")
]
