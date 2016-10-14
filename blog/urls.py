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
    # comment views
    url(r'^page/(?P<pk>\d+)/comment/$', views.add_comment_to_page, name='add_comment_to_page'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]