from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

@api_view(['GET',])
def api_wishlist(request,slug):
    try:
        product = Wishlist.object.get(slug=slug)
    except Wishlist.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer = WishlistSerializer(product)
        return Response(serializer.data)

class WishlistAPI(ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer