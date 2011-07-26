# -*- coding: utf-8 -*-
import inspect

from bencode import bencode

from django.conf import settings
from django.utils import importlib
from django.utils.hashcompat import sha_constructor

from manifesto.manifest import Manifest

__all__ = ['manifest', 'Manifest']


class UnifiedManifest(object):
    def __init__(self):
        self._fallback = []
        self._cache = []
        self._network = []
        self.manifests = []
        self._built = False
        self.excluded_manifests = getattr(settings, 'MANIFESTO_EXCLUDED_MANIFESTS', [])

    def reset(self):
        self._fallback = []
        self._cache = []
        self._network = []
        self.manifests = []
        self._built = False

    def build(self, manifests=None):
        self.reset()

        if manifests == None:
            manifests = self.collect_manifest()

        for manifest in manifests:
            self._fallback += manifest.fallback()
            self._cache += manifest.cache()
            self._network += manifest.network()

        self._built = True

    def collect_manifest(self):
        ignored_classes = [
            Manifest,
        ]
        manifests = []
        for app in settings.INSTALLED_APPS:
            try:
                manifest_module = importlib.import_module("%s.manifest" % app)
            except ImportError:
                continue

            for item_name, item in inspect.getmembers(manifest_module, inspect.isclass):
                if not item in ignored_classes and issubclass(item, Manifest):
                    class_path = "%s.manifest.%s" % (app, item_name)
                    if class_path in self.excluded_manifests:
                        continue
                    manifests.append(item())
        return manifests

    @property
    def fallback(self):
        if not self._built:
            self.build()
        return self._fallback

    @property
    def network(self):
        if not self._built:
            self.build()
        return self._network

    @property
    def cache(self):
        if not self._built:
            self.build()
        return self._cache

    @property
    def revision(self):
        revision = [manifest.revision() for manifest in self.manifests]
        return sha_constructor(bencode(revision)).hexdigest()[:7]

manifest = UnifiedManifest()
