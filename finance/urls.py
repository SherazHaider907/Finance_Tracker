from django.urls import path
from finance.views import RegisterView,DashboardView,TransactionCreateView,TranscationListView,GoalCreateView
urlpatterns = [
    path('register/',RegisterView.as_view(),name="register"),
    path('',DashboardView.as_view(),name="dashboard"),
    path('transaction/add/',TransactionCreateView.as_view(),name="transaction_add"),
    path('transaction',TranscationListView.as_view(),name="transactions_list"),
    path('goal/add/',GoalCreateView.as_view(),name="goal_add"),

]
