from django.db import models

from albums.models import Album
from artists.models import Artist

# Create your models here.

class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	album = models.ForeignKey(Album)
	artist = models.ForeignKey(Artist)

	def player(self):
		return """
		<audio controls>
			<source src="%s" type="audio/mpeg">
			Your browser does not support the audio tag.
		</audio>
		""" % self.track_file.url #pasa la url directa de un archivo

	#las funciones tambien son objetos
	player.allow_tags = True
	#ordenar con funciones en lista
	player.admin_order_field = 'track_file'

	def __unicode__(self):
		return self.title