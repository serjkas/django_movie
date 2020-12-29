from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    """форма отзыва"""
    class Meta:
        model = Reviews
        fields = ('name', 'email', 'text')
