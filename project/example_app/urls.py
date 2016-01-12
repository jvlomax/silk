from django.conf.urls import patterns, url



urlpatterns = ['example_app.views',
               url(r'^$', 'index', name='index')]
