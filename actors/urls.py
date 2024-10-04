from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name='actors_create_list'),
    path('actors/<int:pk>/', views.ActorRetrieveUpdateDestroView.as_view(), name='actor-retrieve-update-view'),
]