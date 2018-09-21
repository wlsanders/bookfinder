from django.db import models

# Create your models here.
class Tags(models.Model):
    tags = models.CharField(max_length=140)



class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    body = models.TextField()
    amazon_link = models.TextField()
    tag = models.ManyToManyField(Tags)
    tagged = models.CharField(max_length=40, default='book')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

