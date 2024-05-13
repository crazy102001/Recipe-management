from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, viewsets, status

from recipe.models import recipe,review
from recipe.serializers import recipeSerializer,UserSerializer,reviewSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView




# Create your views here.

class Recipe(generics.ListCreateAPIView):#Non primary key based
    queryset = recipe.objects.all()
    serializer_class =recipeSerializer


class Recipedetail(generics.RetrieveUpdateDestroyAPIView): # primary key based
    queryset = recipe.objects.all()
    serializer_class = recipeSerializer

class Registerviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        self.request.user.auth_token.delete()

        return Response({'msg':'logout successfully'},status=status.HTTP_200_OK)

class createview(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self,request):
        r=reviewSerializer(data=request.data)

        if(r.is_valid()):
            r.save()
            return Response(r.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class detailrev(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self,pk):
        try:
            return recipe.objects.get(pk=pk)
        except:
            raise Http404

    def get(self,request,pk):
        r=self.get_object(pk)
        rev=review.objects.filter(recipe_name=r)
        revdet=reviewSerializer(rev,many=True)
        return Response(revdet.data)

class cuisinefilter(APIView):
    def get(self,request):
        query=self.request.query_params.get('cuisine')
        recipes=recipe.objects.filter(cuisine=query)
        r=recipeSerializer(recipes,many=True)
        return Response(r.data)

#filter based on meal type


class mealfilter(APIView):
    def get(self,request):
        query = self.request.query_params.get('meal_type')
        recipes = recipe.objects.filter(meal_type=query)
        r = recipeSerializer(recipes, many=True)
        return Response(r.data)

#filter based on ingredients

class IngredientFilter(APIView):
    def get(self,request):
        query = self.request.query_params.get('ingredients')
        recipes = recipe.objects.filter(ingredients=query)
        r = recipeSerializer(recipes, many=True)
        return Response(r.data)

class searchrecipe(APIView):
    # permission_classes=[IsAuthenticated]


    def get(self,request):

        # to get the keyword for search from the request query parameters
        query=self.request.query_params.get('search')
        if(query):
            Recipes=recipe.objects.filter(Q(recipe_name__icontains=query) | Q(recipe_ingredients__icontains=query))
            b=recipeSerializer(Recipes,many=True)
            return Response(b.data)








