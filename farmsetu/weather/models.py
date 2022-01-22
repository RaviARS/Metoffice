from django.db import models


class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.PositiveIntegerField(default=2000)
    jan = models.FloatField(default=0)
    feb = models.FloatField(default=0)
    mar = models.FloatField(default=0)
    apr = models.FloatField(default=0)
    may = models.FloatField(default=0)
    jun = models.FloatField(default=0)
    jul = models.FloatField(default=0)
    aug = models.FloatField(default=0)
    sep = models.FloatField(default=0)
    oct = models.FloatField(default=0)
    nov = models.FloatField(default=0)
    dec = models.FloatField(default=0)
    # win = models.FloatField(default=0)
    win = models.CharField(max_length=28, default=0)
    spr = models.FloatField(default=0)
    sum = models.FloatField(default=0)
    aut = models.FloatField(default=0)
    ann = models.FloatField(default=0)
    region = models.CharField(max_length=28, default="UK")

    def __str__(self):
        return self.region

