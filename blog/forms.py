from django import forms
from .models import Post


# class PostForm(forms.ModelForm):
# 	class Meta:
# 		model = Post
# 		fields = ('title', 'text', 'image_file')
# 		# model = Postfields = ('__all__') # 모든 필드 사용시


class PostForm(forms.Form):
	class Meta:
		author = models.ForeignKey(settings.AUTH_USER_MODEL)
		title = models.CharField(max_length=200)
		text = models.TextField()
		image_file = models.ImageField(upload_to='static_files/upload/%Y/%m/%d')
		created_date = models.DateTimeField(default=timezone.now)
		update_date = models.DateTimeField(blank=True, null = True)




