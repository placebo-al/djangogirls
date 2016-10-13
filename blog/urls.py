from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.page_list, name='page_list'),
    url(r'^page/new/$', views.page_new, name='page_new'),
    url(r'^page/(?P<pk>\d+)/edit/$', views.page_edit, name='page_edit'),
    url(r'^page/(?P<pk>\d+)/$', views.page_detail, name='page_detail'),
]