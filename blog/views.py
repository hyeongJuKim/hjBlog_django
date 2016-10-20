from django.utils import timezone
from django.shortcuts import render
from .models import Post

# lte : less than equal		<=
# lt : less than			<
# gte : greater than equal	>=
# gt : greater than			>

# post의 목록 보여줌
def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
