"""
URL configuration for recipemanagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipe import views
urlpatterns = [
    path('',views.Recipe.as_view()),
    path('Recipe/<pk>',views.Recipedetail.as_view()),
    path('Review/<int:pk>',views.detailrev.as_view()),
    path('create/',views.createview.as_view()),
    path('cuisine/',views.cuisinefilter.as_view()),
    path('meal/',views.mealfilter.as_view()),
    path('ing/',views.IngredientFilter.as_view()),
    path('logout/',views.logout.as_view()),

    ]
