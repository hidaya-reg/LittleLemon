from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = '__all__'
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'

# class GroupNameField(serializers.RelatedField):
#     def to_representation(self, value):
#         # Return the group name
#         return value.name

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']