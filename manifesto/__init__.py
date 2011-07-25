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
        self.fallback = []
        self.cache = []
        self.network = []
        self.manifests = self.collect_manifest()
        self.prepare_manifest()

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
                    manifests.append(item())
        return manifests

    def prepare_manifest(self):
        for manifest in self.manifests:
            self.fallback.extend(manifest.fallback())
            self.cache.extend(manifest.cache())
            self.network.extend(manifest.network())

    @property
    def revision(self):
        revision = [manifest.revision() for manifest in self.manifests]
        return sha_constructor(bencode(revision)).hexdigest()[:7]

manifest = UnifiedManifest()
