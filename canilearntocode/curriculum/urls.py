from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.curriculum, name='curriculum'),
    url(r'^(?P<slug>[\w\d-]+)$', views.subject, name='subject'),
]