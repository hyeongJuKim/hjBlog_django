from django.conf.urls import url
from . import views


urlpatterns = [

    # Main 페이지
    url(r'^main$', views.main, name='main'),

    # About 페이지
    url(r'^$', views.about, name='about'),

	# 블로그 목록
    url(r'^post_list$', views.post_list, name='post_list'),

    # 블로그 상세 페이지
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    # Link 페이지
    url(r'^link$', views.link, name='link'),

]