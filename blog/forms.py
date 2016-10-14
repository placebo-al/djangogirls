from django import forms
from .models import Page, Comment


class PageForm(forms.ModelForm):

	class Meta:
		model = Page
		fields = ('title', 'text', 'slug',)


class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ('author', 'text',)