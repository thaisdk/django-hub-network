from django.urls import path

from . import views

urlpatterns = [
    path('', views.projectsView, name='index'),
    path('projects/',views.galleryView, name='projects'),
    path('project/<str:pk>/', views.singleprojectView, name='project')
]
