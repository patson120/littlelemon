
from django.urls import path

from . import views

app_name='restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),


    path('booking/table', views.BookingViewSet.as_view(), name='booking'),


]