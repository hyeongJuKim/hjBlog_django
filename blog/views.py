from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

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


# post의 상세화면
def post_detail(request, pk):  
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# post의 신규화면
@login_required(login_url='admin:login')  # 로그인 세션이 있을때만 사용 가능
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


# post 수정
@login_required(login_url='admin:login') # 로그인 세션이 있을때만 사용 가능
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def single_photo(request):
	return HttpResponse('1번 사진을 보여드릴게요~!')

# Link 페이지
def link(request):
	return render(request, 'blog/link.html')
