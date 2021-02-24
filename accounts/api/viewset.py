from .serializers import UserSerializer
from rest_framework import viewsets
from accounts.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer