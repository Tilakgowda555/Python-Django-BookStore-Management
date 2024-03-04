from django.db import models


# Create your models here.

class Category(models.Model):
    CategoryName = models.CharField(max_length=40)

    def __str__(self):
        return self.CategoryName


class City(models.Model):
    CityName = models.CharField(max_length=40)

    def __str__(self):
        return self.CityName


class Author(models.Model):
    AuthorName = models.CharField(max_length=50)
    AuthorDob = models.DateField()
    AuthorGender = models.CharField(max_length=20)
    AuthorEmail = models.CharField(max_length=50)
    AuthorPhone = models.CharField(max_length=10)
    AuthorCity = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.AuthorName


class Book(models.Model):
    BookName = models.CharField(max_length=50)
    BookDescription = models.CharField(max_length=500)
    BookPublishedOn = models.DateField()
    BookPrice = models.IntegerField(default=0)
    BookAuthor = models.ForeignKey(Author, on_delete=models.CASCADE)
    BookCategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.BookName

