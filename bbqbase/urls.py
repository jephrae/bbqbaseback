#bbqbase urls.py

from django.urls import path
from . import views


urlpatterns = [
       path('', views.RecipeList.as_view(), name='recipe_list'),
       path('recipes/', views.RecipeList.as_view(), name='recipe_list'),
       path('recipes/<int:pk>', views.RecipeDetail.as_view(), name='recipe_detail'),
]