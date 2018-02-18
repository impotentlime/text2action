from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^test/$', views.test_template, name = 'test_template'),
    url(r'^try/$', views.ang, name = 'ang'),
    url(r'^final/$', views.final, name='final'),
]
