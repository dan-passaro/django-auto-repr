from django.db import models
from django_auto_repr import AutoRepr


WIDGET_COLORS = [
    ('green', 'Green'),
    ('blue', 'Blue'),
    ('yellow', 'Yellow'),
]


class Widget(AutoRepr, models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)
    color = models.CharField(max_length=100, choices=WIDGET_COLORS, default=WIDGET_COLORS[0][0])
