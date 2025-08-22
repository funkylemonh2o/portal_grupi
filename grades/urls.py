from django.urls import path
from . import views

app_name = 'grades'

urlpatterns = [
    path('my-grades/', views.student_grades, name='student_grades'),
    path('', views.all_grades, name='all_grades'),
]