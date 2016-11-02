from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    # Main 페이지 (url없을 때)
    url(r'^$', views.main, name='main'),

    # Main 페이지
    url(r'^main$', views.main, name='main'),

    # About 페이지
    url(r'^about$', views.about, name='about'),

    
	# 블로그 목록
    url(r'^post_list$', views.post_list, name='post_list'),

    # 블로그 상세 페이지
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    # 블로그 신규 작성 페이지
    url(r'^post/new/$', views.post_new, name ='post_new'),

    # 블로그 수정
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),


    # Link 페이지
    url(r'^link$', views.link, name='link'),

]

# settings.py의 MEDIA_ROOT의 이름을 넣는다.
urlpatterns += static('media', document_root=settings.MEDIA_ROOT)
