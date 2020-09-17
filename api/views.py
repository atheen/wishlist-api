from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from items.models import Item,FavoriteItem
from .serializers import ItemsSerializer,RegisterSerializer,ItemDetailsSerializer

from .permissions import IsOwner

class APIRegister(CreateAPIView):
	serializer_class = RegisterSerializer

class ItemsList(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemsSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name','description']


class ItemDetails(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes= [IsOwner]
