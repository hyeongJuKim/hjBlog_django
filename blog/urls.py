from django.conf.urls import url
from . import views


urlpatterns = [

	# 블로그 목록
    url(r'^$', views.post_list, name='post_list'),

]