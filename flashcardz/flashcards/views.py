from django.http import Http404
from .models import Card
from .serializers import CardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers


# Create your views here.
class CardList(APIView):
    def get(self, request):
        card = Card.objects.all()
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CardCollection(APIView):
    def get(self, request, stack_id):
        card = Card.objects.all().filter(stack=stack_id)
        serializer = CardSerializer(card, many=True)
        return Response(serializer.data)


class CardDetail(APIView):
    def get_by_pk(self, pk):
        try:
            return Card.objects.get(pk=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        card = self.get_by_pk(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def put(self, request, pk):
        card = self.get_by_pk(pk)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_by_pk(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
