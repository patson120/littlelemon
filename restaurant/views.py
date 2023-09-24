from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from . import models, serializers
from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def home(request):
    return render(request, 'restaurant/index.html')


class MenuItemView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer



class BookingViewSet(viewsets.ViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response(dict(message="This view is protected"), status=status.HTTP_403_FORBIDDEN)