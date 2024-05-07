from django.db import models


class Rect(models.Model):
    name = models.CharField(max_length=30)


class Segment(models.Model):
    rect = models.ForeignKey(Rect, on_delete=models.CASCADE, related_name='rect')
    x1 = models.FloatField()
    y1 = models.FloatField()
    x2 = models.FloatField()
    y2 = models.FloatField()

