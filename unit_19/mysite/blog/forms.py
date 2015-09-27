from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm): 
    class Meta: 
        model = Comment 
        exclude = ["post"]