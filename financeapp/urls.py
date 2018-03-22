from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'financeapp'
urlpatterns = [
    # ex: /
    path('', views.home, name='home'),
    # ex:
    path('incomes/', views.Incomes.as_view(), name='incomes'),
    # ex:
    path('expenses/', views.Expenses.as_view(), name='expenses'),
    # ex:
    path('analysis/', views.analysis, name='analysis'),
    # ex:
    path('savings/', views.Savings.as_view(), name='savings'),
    # ex:
    path('incomes/add_income', views.add_income, name='add_income'),
]
