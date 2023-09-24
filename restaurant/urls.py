
from django.urls import path

from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name='restaurant'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu_items/', views.MenuItemView.as_view(), name='menu_items'),
    path('menu_items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu_item'),
    path('message/', views.msg, name='message'),
    path('api-auth-token/', obtain_auth_token),

    path('booking/table', views.BookingViewSet.as_view({"get": 'list'}), name='booking'),


]