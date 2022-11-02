from contextlib import nullcontext
from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    surname = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=200, blank=False, null=False)
    descriptio = models.TextField(blank=False, null=False)


