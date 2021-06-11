from django.db import models

# Create your models here.
class Event(models.Model):
     event_image = models.ImageField(upload_to = 'event_images/')
     event_text = models.CharField(max_length = 300)

     def __str__(self): #При помощи этой функции обеспечиваем отображение в админ-панели 8000/admin названий event постов, а не просто абстрактной нумерации.
         return self.event_text
