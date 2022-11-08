from django.db import models


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    surname = models.CharField(max_length=200, blank=False, null=False)
    nationality = models.CharField(max_length=200, blank=False, null=False)
    descriptio = models.TextField(blank=False, null=False)
    creation_date = models.DateField('Creation Date', auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']
        
    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=200, blank=False, null=False)
    publication_date = models.DateField('Publication Date', blank=False, null=False)
    author_id = models.ManyToManyField(Author)
    creation_date = models.DateField('Creation Date', auto_now = True, auto_now_add = False)
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ["title"]
        
    def __str__(self) -> str:
        return self.title


