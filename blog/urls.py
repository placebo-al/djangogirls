from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.page_list, name='page_list'),
    url(r'^page/new/$', views.page_new, name='page_new'),
    url(r'^page/(?P<pk>\d+)/edit/$', views.page_edit, name='page_edit'),
    url(r'^page/(?P<pk>\d+)/$', views.page_detail, name='page_detail'),
    url(r'^page/(?P<pk>\d+)/publish/$', views.page_publish, name='page_publish'),
    url(r'^page/(?P<pk>\d+)/remove/$',views.page_remove, name='page_remove'),
    url(r'^drafts/$', views.page_draft_list, name='page_draft_list'),
]