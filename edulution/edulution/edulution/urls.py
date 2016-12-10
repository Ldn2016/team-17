from django.conf.urls import url

from . import views

urlpatterns = [
    # /student/
    url(r'^$', views.index, name='index'),
    # /student/...
    url(r'^subjects/$', views.index, name='index'),

]
