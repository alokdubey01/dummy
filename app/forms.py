from django import forms
from .models import *
from ckeditor.fields import RichTextField


class PostForm(forms.ModelForm):
    # userName = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    title = forms.CharField(widget=forms.TextInput(),required=True, max_length=100)
    content = RichTextField()

    class Meta:
        model  = Posts
        fields = ('title','content',)