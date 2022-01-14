from django.db import models

# Create your models here.

class Doc( models.Model):
    model = models.ImageField(upload_to='images/')

    def __str__ (self):
        return str(self.pk)
