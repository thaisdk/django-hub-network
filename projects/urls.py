from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeView, name='index'),  # Root 
    path('projects/',views.projectsView, name='projects'),
    path('project/<str:pk>/', views.projectView, name='project'),
    # path('like/<str:pk>', views.like, name='like'),
    # path('like/<str:pk>', views.like, name='dislike'),

]
