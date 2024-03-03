from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from restaurant.models import Bookings, Menu
from restaurant.serializers import BookingSerializer, MenuSerializer


def index(request):
    return render(request, 'index.html')


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
