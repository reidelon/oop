from django.db import models
from django.core.exceptions import ValidationError


class Common(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()


class CommonIntString(Common):
    default = models.CharField(max_length=200)
    mandatory = models.BooleanField()


class String(CommonIntString):
    length = models.PositiveIntegerField()

    def __str__(self):  # __unicode__ on Python 2
        return str(self.length)


# def validate_even(value, min):
#     if value % 2 != 0:
#         raise ValidationError('%s is not an even number' % value)


class Integer(CommonIntString):
    min = models.BigIntegerField()
    max = models.BigIntegerField()
    # max = models.BigIntegerField(validators=[validate_even, self.min])
    

    def __str__(self):  # __unicode__ on Python 2
        return self.min + '' + self.mandatory


class Enum(Common):
    key = models.IntegerField(unique=True)
    value = models.CharField(max_length=200)
