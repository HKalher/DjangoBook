from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 60)
    state_province =models.CharField(max_length = 50)
    country = models.CharField(max_length = 50)
    website = models.URLField()
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.EmailField()
    def __str__(self):
        return u'%s %s' % (self.first_name,self.last_name)

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author) # becuase an author can write several books
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    edition = models.CharField(max_length = 20,null= True)
    ISBN = models.CharField(max_length = 20)
    def __str__(self):
        return self.title

