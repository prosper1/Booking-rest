from django.shortcuts import render
from .serializers import BookingSerializer, ItemSerializer, RestaurantSerializer, MediaSerializer
from .models import Item, Booking, Restaurant, Media
from rest_framework import viewsets

# Create your views here.

class ItemsViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class MediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
