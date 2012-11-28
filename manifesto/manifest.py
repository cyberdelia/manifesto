# -*- coding: utf-8 -*-
from bencode import bencode
import itertools

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
        revision = list(itertools.chain(self.fallback(), self.network(), self.cache()))
        return sha1(bencode(revision)).hexdigest()[:7]
