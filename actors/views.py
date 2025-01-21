from rest_framework import generics
from .models import Actor
from .serializers import ActorSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ActorListCreateView(generics.ListCreateAPIView):
    authentication_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
