from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.page_list, name='page_list'),
    url(r'^page/(?P<pk>\d+)/$', views.page_detail, name='page_detail'),
]