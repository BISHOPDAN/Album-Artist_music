from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django_countries.fields import CountryField


AlbumFormat_CHOICES = (
    ('LP', 'LP'),
    ('CD', 'CD'),
    ('MP3', 'MP3'),
    ('FLAC', 'FLAC'),
)

Genre_CHOICES = (
    ('Afro', 'Afro'),
    ('Blues', 'Blues'),
    ('Gospel', 'Gospel'),
    ('Hip hop', 'Hip hop'),
    ('Jazz', 'Jazz'),
    ('Metal', 'Metal'),
    ('Others', 'Others'),
    ('R & B', 'R & B'),
    ('Rock', 'Rock'),
    ('Electronic', 'Electronic'),
    ('Caribbean', 'Caribbean'),
)

class Artist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField()
    country_of_origin = CountryField(null=True, blank=True)
    profile_picture = models.ImageField(default='profile.jpeg',null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]

    def age(self):
        today = datetime.now().date()
        return (today - self.date_of_birth).days // 365



class Album(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    Album_description = models.CharField(max_length=500)
    album_title = models.CharField(max_length=500)
    Year_of_release = models.PositiveSmallIntegerField()
    genre =models.CharField(max_length=20, choices=Genre_CHOICES)
    album_format = models.CharField(max_length=20, choices=AlbumFormat_CHOICES)
    album_logo_link=models.CharField(max_length=1000)
    is_favorite_album = models.BooleanField(default=False)
    
    def __str__ (self):
        return self.album_title

class Song(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title= models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__ (self):
        return self.song_title
     
# PROFILE MODEL
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    fav_genre=models.CharField(max_length=50)
    profile_image = models.ImageField(default='profile.jpeg',null=True, blank=True)

class Watchlater(models.Model):
    watch_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.TextField(default="")