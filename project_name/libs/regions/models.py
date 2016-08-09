"""
"""
from django.db import models


class Country(models.Model):
    """
    """
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ("code",)

    def __str__(self):
        return '%s: %s' % (self.code, self.name)


class State(models.Model):
    """
    """
    country = models.ForeignKey(Country, related_name='states')
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("code",)

    def __str__(self):
        return '%s> %s: %s' % (self.country.code, self.code, self.name)


class City(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='cities')
    state = models.ForeignKey(State, related_name='cities')
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return '%s> %s> %s' % (self.country.code, self.state.code, self.name)
