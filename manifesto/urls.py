# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *  # noqa

from manifesto.views import ManifestView


urlpatterns = patterns('',
    url(r'^manifest\.appcache$', ManifestView.as_view(), name="cache_manifest"),
)
