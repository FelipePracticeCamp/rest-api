from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer


# Create your views here.
class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
