from django.db import models

# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length = 200)
    post_date = models.DateField()
    post_time = models.DateTimeField()
    post_image = models.ImageField(upload_to = 'post_images/')
    post_text = models.CharField(max_length = 500)

    def get_summary(self):
        print('get_summary(' + str(self) + 'called')
        return self.post_text[:70] + '...'

    def __str__(self):
        return self.post_title

