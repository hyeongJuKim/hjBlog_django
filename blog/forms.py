from django import forms
from .models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', 'image_file')
		# model = Postfields = ('__all__') # 모든 필드 사용시

