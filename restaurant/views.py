from django.shortcuts import render

from rest_framework.generics import ListCreateView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets
from . import models, serializers
from django.contrib.auth.models import User
from django.contrib.auth.

# Create your views here.

def home(request):
    return render(request, 'restaurant/index.html')


class MenuItemView(ListCreateView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.MenuItem.objects.all()
    serializer_class = serializers.MenuItemSerializer



class BookingViewSet(viewsets.ViewSet):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    Permission_classes = [permissions.IsAuthenticated]