from pydoc import describe
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='anonymous')
    email = models.EmailField(blank=True)
    describe = models.TextField(default='This is Library Application')
    
    def __str__(self):
        return self.name
    
    
# From the above code, Django will make a table in a database named book. That table will have these fields:

# Name, picture, author, email, and description of the book object. From this class, we can easily manipulate the table. The important part here is the picture field. It is set as ImageField.

# This ImageField is the reason why we installed pillow in this virtual environment. Django by default uses pillow to handle Images in ImageField. So, that was the models of our book app.