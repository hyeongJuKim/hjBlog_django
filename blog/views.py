from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

# lte : less than equal		<=
# lt : less than			<
# gte : greater than equal	>=
# gt : greater than			>


# Main페이지
def main(request):
	return render(request, 'blog/main.html')


# About페이지
def about(request):
	return render(request, 'blog/about.html')


# post의 목록 보여줌
def post_list(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts': posts})


# post의 상세 화면
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# Link 페이지
def link(request):
	return render(request, 'blog/link.html')
