from django.urls import path

from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.course_create, name='course_create'),
    path('delete/<int:course_id>', views.course_delete, name='course_delete'),
    path('show/<int:course_id>', views.course_show, name='course_show'),
]
