from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from datetime import datetime

from items.models import Item,FavoriteItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name', 'last_name']

class ItemsSerializer(serializers.ModelSerializer):
    favourited = serializers.SerializerMethodField()
    added_by= UserSerializer()
    detail = serializers.HyperlinkedIdentityField(
        view_name = "api-detail",
        lookup_field = "id",
        lookup_url_kwarg = "item_id"
    )
    class Meta:
        model = Item
        fields = ['image', 'name', 'description','detail','added_by','favourited']

    def get_favourited(self, obj):
        user = obj.user
        favourited = user.item_set.all()


class ItemDetailsSerializer(serializers.ModelSerializer):
    favourited_by=serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields = ['image', 'name', 'description', 'favourited_by']

    def get_favourited_by(self, obj):
        items = FavoriteItem.objects.filter(item=obj)
        user = items.user
        return user.data
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data
