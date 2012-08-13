# -*- coding: utf-8 -*-
from django.test import TestCase


class ManifestViewTest(TestCase):
    urls = "manifesto.urls"

    def test_manifest_render(self):
        response = self.client.get('/manifest.appcache')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/cache-manifest')
        self.assertTemplateUsed(response, "manifesto/manifest.appcache")
        context = response.context
        self.assertEqual(context['revision'], '593b743')
        self.assertEqual(context['cache_list'], ['/static/js/application.js',
            '/static/css/screen.css'])
        self.assertEqual(context['network_list'], ['*'])
        self.assertEqual(context['fallback_list'], [('/', '/offline.html')])
