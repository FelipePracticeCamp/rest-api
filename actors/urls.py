
from django.urls import path
from .views import ActorListCreateView, ActorRetrieveUpdateDestroyView

urlpatterns = [
    path("actors_list/", ActorListCreateView.as_view(), name='actors_list'),
    path("actors/<int:pk>/", ActorRetrieveUpdateDestroyView.as_view(), name='actors_retrieve')
]
