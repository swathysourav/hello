from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile
# Create your models here.
class Post(models.Model):
    movie_name=models.CharField(max_length=250)
    movie_description=models.TextField(null=True)
    release_date = models.DateField(null=True,blank=True)
    movie_image=models.ImageField(null=True,blank=True,upload_to='gallery')
    movie_user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    actors=models.CharField(max_length=250)
    youtube=models.CharField(max_length=250)
    def __str__(self):
        return self.movie_name
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})




class ReviewRating(models.Model):
    movie_title=models.ForeignKey(Post,null=True,on_delete=models.CASCADE)
    review=models.TextField(max_length=250,blank=True)
    rating=models.FloatField()
    def __str__(self):
        return self.rating
    def get_absolute_url(self):
       return reverse('post-review',kwargs={'pk':self.pk})
