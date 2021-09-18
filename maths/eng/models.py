from django.db import models


class Book(models.Model):
    ISBN=models.CharField(max_length=50)
    title = models.CharField(max_length = 50)
    author = models.CharField(max_length = 50)
    edition = models.IntegerField(default= 2001)
    publication = models.CharField(default='',max_length= 50)

class Meta:
    db_table = "book"
