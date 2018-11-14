# coding: utf-8
from django.conf.urls import patterns, url

from debug_toolbar.views import render_panel

urlpatterns = patterns('',
    url(r'render_panel/', render_panel, name='render_panel'),
)
