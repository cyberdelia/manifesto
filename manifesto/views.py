# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView

from manifesto import manifest


class ManifestView(TemplateView):
    template_name = "manifesto/cache.manifest"

    def render_to_response(self, context, **kwargs):
        kwargs['content_type'] = 'text/cache-manifest'
        return super(ManifestView, self).render_to_response(context, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'revision': manifest.revision,
            'cache_list': manifest.cache,
            'network_list': manifest.network,
            'fallback_list': manifest.fallback,
        })
        return kwargs
