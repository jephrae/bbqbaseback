from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id','name','meat_type','meat_cut','cooktime','temp','credit','photo_url','desc','instructions',)