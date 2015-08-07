from django.conf.urls import url, patterns

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^start/$', views.start, name='start'),
    url(r'^find/$', views.find, name='find'),
    url(r'^end/$', views.end, name='end'),
    url(r'^startsesh/$', views.startsesh, name='startsesh'),

]