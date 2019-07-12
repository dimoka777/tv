from _datetime import datetime
from django.db import models
from django.urls import reverse


class Choice(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=255)
    price = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{}".format(self.name)


class Post(models.Model):
    tv_choices = models.ForeignKey('Choice', related_name="posts", on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    order_date = models.DateTimeField(default=datetime.now)
    post_dates = models.IntegerField()
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    reception = models.BooleanField(default=False)


    def __str__(self):
        return '{}{}{}'.format(self.text,self.order_date, self.price, )
