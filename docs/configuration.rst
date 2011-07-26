.. _ref-configuration:

=============
Configuration
=============

Configuration and list of available settings for Manifesto.

Excluding manifests
===================

You can exclude manifest from the final cache-manifest with ``MANIFESTO_EXCLUDED_MANIFESTS`` ::

	MANIFESTO_EXCLUDED_MANIFESTS = (
		'randomapp.manifest.WrongManifest',
	)

**Default:** []
	