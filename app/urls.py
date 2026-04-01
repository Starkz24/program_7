from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_form),
    path('delete/', views.delete_unpaid),
]