from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import AllowAny

# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes =(AllowAny,)

    # def post(self, request, form=None):
    #     return(Response())
    #     serializer = RecipeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer