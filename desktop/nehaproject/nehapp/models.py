from django.db import models

class Movie(models.Model):
    actor = models.CharField(max_length = 30)
    actor_movie = models.CharField(max_length = 50)
    genre = models.CharField(max_length = 100)
    movie_logo = models.CharField(max_length = 100)
    def __str__(self):
        return self.actor+'    '+self.actor_movie+'  '+self.genre+' '+self.movie_logo
class Songs(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 50)
    song_name = models.CharField(max_length = 100)
    is_favorite = models.BooleanField(default = False)
    def __str__(self):
        return self.file_type+'    '+self.song_name

class Details(models.Model):
    First_Name = models.CharField(max_length = 50)
    Last_Name = models.CharField(max_length = 50)
    email_id = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    def __str__(self):
        return self.email_id+'    '+self.password

    
# Create your models here.

