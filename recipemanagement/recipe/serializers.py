from django.contrib.auth.models import User
from rest_framework import serializers

from recipe.models import recipe,review


class recipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=recipe
        fields=['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self,validated_data):

        u=User.objects.create_user(username=validated_data['username'],password=validated_data['password'])
        u.save()
        return u

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=review
        fields=['recipe_name','user','rating','comments']