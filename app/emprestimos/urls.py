from django.urls import path

from app.emprestimos import views

app_name = 'emprestimos'

urlpatterns=[
    path('', views.home, name='home')
]