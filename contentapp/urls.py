from django.conf.urls import url
from . import views

app_name = 'contentapp'

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
    url(r'^news_detail/(?P<id>[-\w]+)/$', views.news_detail_view, name='news_detail'),
    url(r'^news/$', views.news_view, name='news'),
    url(r'^files/$', views.files_view, name='files'),
    url(r'^search/$', views.search_result_view, name='search_result'),
]