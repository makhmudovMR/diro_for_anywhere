from django.conf.urls import url


from . import views

app_name = 'main'

urlpatterns = [
    url(r'^hello/$', views.hello_view, name='hello'),
    url(r'^$', views.main_view, name='main'),
    url(r'^test/$', views.test_view, name='test'),
    url(r'^question/(?P<id>[-\w]+)/$', views.question_view, name='questions'),
    url(r'^user_panel/$', views.user_panel_view, name='user_panel'),
    url(r'^test_result_view/(?P<id>[-\w]+)/$', views.test_result_view, name='test_result'),


    url(r'^all_users/$', views.all_users_view, name='all_users'),
    url(r'^users_tests/(?P<id>[-\w]+)/$', views.users_tests_view, name='users_tests'),
    url(r'^user_test_result/(?P<id>[-\w]+)/$', views.user_test_result_view, name='user_test_result'),


    url(r'^signin/$', views.sign_in_view, name='sign_in'),
    url(r'^signup/$', views.sign_up_view, name='sign_up'),
    url(r'^logout/$', views.logout_from_system, name='logout'),

    url(r'^handletest/$', views.handle_test, name='handle_test'),
]