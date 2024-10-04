from django.db import models
from musician.models import MusicianModel
# Create your models here.
class AlbumModel(models.Model):
    ALBUM_RATINGS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    Album_Name = models.CharField(max_length=100,verbose_name="Album Name")
    Album_release_date = models.DateField(verbose_name=" Album_release_date")
    Rating_between =models.CharField(max_length=1,choices=ALBUM_RATINGS)
    musician = models.ForeignKey(MusicianModel, related_name="albums",on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.Album_Name