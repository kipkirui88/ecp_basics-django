from django.db import models

# Create your models here.
class person(models.Model):
    id_no = models.IntegerField()
    name = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "person"    