# -*- coding: utf-8 -*-
import itertools
import pickle

try:
    from hashlib import sha1
except ImportError:
    from django.utils.hashcompat import sha_constructor as sha1


class Manifest(object):
    def fallback(self):
        return []

    def network(self):
        return ['*']

    def cache(self):
        return []

    def revision(self):
        manifest = list(itertools.chain(self.fallback(), self.network(), self.cache()))
        revision = pickle.dumps(manifest, pickle.HIGHEST_PROTOCOL)
        return sha1(revision).hexdigest()[:7]
