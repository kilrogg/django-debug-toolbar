from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r"^$", TemplateView.as_view(template_name="index.html")),
    url(r"^jquery/$", TemplateView.as_view(template_name="jquery/index.html")),
    url(r"^mootools/$", TemplateView.as_view(template_name="mootools/index.html")),
    url(r"^prototype/$", TemplateView.as_view(template_name="prototype/index.html")),
    url(r"^admin/", admin.site.urls),
    url(r"^__debug__/", include('debug_toolbar.urls', namespace='djdt'))
)
