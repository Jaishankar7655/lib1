from django.db import models

# Create your models here.
class Books(models.Model):
    Book_Title  = models.CharField(max_length=100)
    Author_name = models.CharField(max_length=100)
    ISBN_Number = models.CharField(max_length=100)
    Book_Description = models.TextField()
    Genre = models.CharField(max_length=100)
    Publisher = models.CharField(max_length=100)
    Publication_Year = models.CharField(max_length=10)
    copies_available = models.IntegerField()
    rack_number = models.CharField(max_length=100)
    Book_Url = models.URLField()
    thumbnail = models.ImageField(upload_to='images/')
    Book_PDF = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.Book_Title