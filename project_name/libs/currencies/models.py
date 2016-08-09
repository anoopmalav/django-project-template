from django.db import models


class Currency(models.Model):
    """
    """
    name = models.CharField(max_length=60)
    icon = models.ImageField(upload_to='currency')
    code = models.CharField(max_length=10)
    symbol = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return "%s: %s" % (self.code, self.name)
