from django.db import models

# Create your models here.
class data(models.Model):
    srNo = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name