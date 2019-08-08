"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'learning_logs'

urlpatterns =[
        #Home Page
        path('', views.index, name = 'index'),
        url('^test/$', views.test, name = 'test'),
        
        #show all topics.
        url(r'^topics/$', views.topics, name = 'topics'),
        
        #detail page for a single topic
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        #       ?P<topic_id>\d+) This matches an integer and stores the integer 
        #         value in the argument topic_id     
        
        # Page for adding a new topic
        url(r'^new_topic/$', views.new_topic, name='new_topic'),
        
        # Page for adding entry
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
           
        # Page for editing an entry
        url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
