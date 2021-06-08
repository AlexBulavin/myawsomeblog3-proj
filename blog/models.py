from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_date = models.DateField()
    post_time = models.DateTimeField()
    post_image = models.ImageField(upload_to = 'post_images/')
    post_text = models.CharField(max_length = 500)

    def get_summary(self):
        return self.text[:70]
    #print('Class Post called')

