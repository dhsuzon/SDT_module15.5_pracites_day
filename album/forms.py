from django import forms
from .models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
      model = AlbumModel
      fields ='__all__'
      widgets = {
          "Album_release_date":forms.DateInput(attrs={'type':'date'}),
          "Rating_between":forms.RadioSelect()
      }
      
      
      
      