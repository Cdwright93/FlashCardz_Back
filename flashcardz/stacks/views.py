from django.http import Http404
from .models import Stack
from .serializers import StackSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from corsheaders.defaults import default_methods
from corsheaders.defaults import default_headers


# Create your views here.
class StackList(APIView):
    def get(self, request):
        stack = Stack.objects.all()
        serializer = StackSerializer(stack, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class StackDetail(APIView):
    def get_by_pk(self, pk):
        try:
            return Stack.objects.get(pk=pk)
        except Stack.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stack = self.get_by_pk(pk)
        serializer = StackSerializer(stack)
        return Response(serializer.data)

    def put(self, request, pk):
        stack = self.get_by_pk(pk)
        serializer = StackSerializer(stack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stack = self.get_by_pk(pk)
        stack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
