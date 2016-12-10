from django.conf.urls import url

from . import views

urlpatterns = [
    # /student/
    url(r'^$', views.login, name='login'),
    # /student/...
    url(r'^subjects/$', views.subjects, name='subjects'),

]
