
from django import forms

from .models import *

class ReporterForm(forms.ModelForm):
    class Meta:
        model = Reporter
        fields = ['full_name']

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content', 'reporter']
    
class UpdateArticleForm(forms.ModelChoiceField):
    custom_field = forms.CharField(required=False) 
    class Meta:
        model = Article
        fields = ['pub_date', 'headline', 'content']

  
