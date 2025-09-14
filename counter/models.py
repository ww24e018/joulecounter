from django.db import models

class FoodItemTemplate(models.Model):
    name = models.CharField(max_length=100)
    modifier = models.CharField(max_length=100, blank=True)
    joules = models.PositiveIntegerField()

    class Meta:
        unique_together = ('name', 'modifier')

    def __str__(self):
        return f"{self.name} ({self.modifier})" if self.modifier else self.name


class FoodItemLog(models.Model):
    template = models.ForeignKey(FoodItemTemplate, on_delete=models.CASCADE)
    eaten_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.template} @ {self.eaten_at:%Y-%m-%d %H:%M}"
