from django.urls import path
from .views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path("reviews_list", ReviewListCreateView.as_view(), name='reviews_list'),
    path("reviews/<int:pk>/", ReviewRetrieveUpdateDestroyView.as_view())
]
