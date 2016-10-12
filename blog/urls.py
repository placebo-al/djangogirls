from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.page_list, name='page_list'),
]