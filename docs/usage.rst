.. _ref-usage:

=====
Usage
=====

Describes how to use Manifesto when it is installed and configured.

Creating a manifest 
===================

To add a manifest in your application, you need to add a ``manifest`` module in it.
Inside this module you can create any number of manifest as long as they inherit 
from ``Manifest`` class.

::
	
	from manifesto import Manifest
	
	
	class StaticManifest(Manifest):
	  def cache(self):
	    return [
	      '/static/js/application.js',
	      '/static/css/screen.css',
	    ]

	  def network(self):
	    return ['*']
		
	  def fallback(self):
	    return [
	      ('/', '/offline.html'),
	    ]

.. note ::
	
	The meaning of each method is corresponding to each section of a cache-manifest,
	see `Offline Web applications documentation <http://www.whatwg.org/specs/web-apps/current-work/multipage/offline.html>`_ 
	for reference.


By default, a revision is calculated for each manifest, if you want to override
the way we calculate revision, you just need to add a ``revision`` method to
your manifest ::

	import time
	from manifesto import Manifest


	class StaticManifest(Manifest):
	  def revision(self):
	    return int(time.time())


Access to the final cache-manifest
==================================

Manifesto provides a default ``ManifestView`` and ``urls`` to link to the final
cache-manifest ::

	from django.conf.urls.defaults import *	
	from manifesto.views import ManifestView


	urlpatterns = patterns('',
	  url(r'^cache\.manifest$', ManifestView.as_view(), name="cache_manifest"),
	)

Then from your template, you can link to your cache-manifest ::

	<!doctype html>
	<html manifest="{% url cache_manifest %}">
	 <head>
	  <meta charset="utf-8">

