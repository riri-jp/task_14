from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from api.serializer import ListSerializer


class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = ListSerializer