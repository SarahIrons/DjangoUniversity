from django.db import models
from django import utils


class UniversityCampus(models.Model):
    campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    state= models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    class Meta:
        verbose_name_plural = "University Campus"

    def __str__(self):
        campus_Name = '{0.campus_Name}: {0.state}'
        return campus_Name.format(self)
