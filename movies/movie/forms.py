from movie.models import Movie
from django import forms


class Movieform(forms.ModelForm):
    class Meta:

        model=Movie
        fields="__all__"