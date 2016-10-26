from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model): # Model class를 상속받은 Post class를 생성한다는 뜻
	# 게시 Model. 5개읠 필드를 만듬.
	author = models.ForeignKey(settings.AUTH_USER_MODEL)
	title = models.CharField(max_length=200)
	text = models.TextField()
	image_file = models.ImageField()
	created_date = models.DateTimeField(default=timezone.now)
	update_date = models.DateTimeField(blank=True, null = True)

	def update(self):
		# 수정일자
		self.update_date = timezone.new()
		self.save()

	def __str__(self):
		return self.title