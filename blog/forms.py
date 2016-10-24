from django import forms
from .models import Post


class PostForm(forms.modelForm):

	class Meta:
		model = Postfields = ('title', 'text',)
		# model = Postfields = ('__all__') # 모든 필드 사용시
