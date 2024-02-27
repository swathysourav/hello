from django import forms
from . models import Post,ReviewRating

class ImageForm(forms.ModelForm):
   class Meta:
        model = Post
        fields = ['movie_image','movie_name','movie_description', 'release_date', 'actors','movie_user', 'youtube']
class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields=['movie_title','review','rating']
