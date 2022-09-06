from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from cart.serializers import *

class CartView(generics.ListAPIView):
    serializer_class = CartSerializer
    
    def get_queryset(self):
        """
        return a list of all records for
        the user as determined by the userID portion of the URL.
        """
        userID = self.kwargs['id']
        return Cart.objects.filter(user_id=userID)

class CartUpdateView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    
    def update(self, request, *args, **kwargs):
        cartID = self.kwargs['pk']
        serializer = Cart.objects.filter(id=cartID)
        return Response(serializer.data)