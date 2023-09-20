from django import forms
from .models import Comment

class CommentForm(forms.Form):
    id = forms.CharField(initial='{{ element.author }}')
    text = forms.CharField()
