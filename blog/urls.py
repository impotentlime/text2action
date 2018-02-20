from django.conf.urls import url
from .import views

urlpatterns = [
    # url(r'^$', views.post_list, name = 'home'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    # url(r'^post/new/$', views.post_new, name='post_new'),

    url(r'^$', views.final_list, name = 'final_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.final_detail, name='final_detail'),
    url(r'^new/$', views.final_new, name='final_new'),

    # url(r'^test/(?P<pk>[0-9]+)/$', views.test, name='test'),
]
