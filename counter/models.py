import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db import models
from django.http import HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods


class FoodItemTemplate(models.Model):
    name = models.CharField(max_length=100)
    modifier = models.CharField(max_length=100, blank=True)
    joules = models.PositiveIntegerField()

    class Meta:
        unique_together = ('name', 'modifier')

    def __str__(self):
        return f"{self.name} ({self.modifier})" if self.modifier else self.name

    #   --- static helpers -------------------------------------------------
    @staticmethod
    @require_http_methods(["GET"])
    @login_required
    def export_view(request):
        return JsonResponse(
            json.loads(serializers.serialize('json', FoodItemTemplate.objects.all())),
            safe=False
        )

    @staticmethod
    @require_http_methods(["POST"])
    @login_required
    def import_view(request):
        try:
            for obj in serializers.deserialize('json', request.body):
                obj.save()
        except Exception as e:
            return HttpResponseBadRequest(str(e))
        return JsonResponse({'status': 'ok'})


class FoodItemLog(models.Model):
    template = models.ForeignKey(FoodItemTemplate, on_delete=models.CASCADE)
    eaten_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.template} @ {self.eaten_at:%Y-%m-%d %H:%M}"
