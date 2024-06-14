from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name}"

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_consume")
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE, related_name = "food_consume")

    def __str__(self):
        return f"{self.food_consumed.name}"