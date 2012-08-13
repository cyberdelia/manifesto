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
