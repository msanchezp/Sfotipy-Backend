from django.contrib import admin

from .models import Track

from actions import export_as_excel

# Register your models here.

class TrackAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'order', 'album', 'player', 'es_pharrell')
	list_filter = ('artist', 'album')
	#se agrega __ (doble underscore) cuando se trabaja con claves foraneas
	search_fields = ('title', 'artist__first_name', 'artist__last_name')
	list_editable = ('album',)
	actions = (export_as_excel,)
	raw_id_fields = ('artist', )

	def es_pharrell(self, obj):
		return obj.id == 1
	es_pharrell.boolean = True;

admin.site.register(Track, TrackAdmin)