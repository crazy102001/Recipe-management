from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
class recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    recipe_ingredients=models.CharField(max_length=140)
    instructions=models.TextField()
    cuisine=models.CharField(max_length=40)
    meal_type=models.CharField(max_length=20)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.recipe_name


class review(models.Model):
    recipe_name=models.ForeignKey(recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.DecimalField(max_digits=2,decimal_places=1,validators=[MinValueValidator(0.0),MaxValueValidator(5.0)])
    comments=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe_name.recipe_name


