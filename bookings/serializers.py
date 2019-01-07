from rest_framework import serializers
from .models import Item, Restaurant, Booking, Media

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ('name','quantity','price','available','notes','item_pic')

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = ('user_firstname','user_lastname','user_email','user_cell',
        'id_number','date','item','adults','children')

class RestaurantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Restaurant
        fields = ('meal_name','price','category','display_pic')

class MediaSerializer(serializers.ModelSerializer):

    class Meta:
        models = Media
        fields = ('display_pic')
