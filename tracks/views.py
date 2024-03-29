import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
# Create your views here.

def track_view(request, title):
	"""try:
		track = Track.objects.get(title=title)
	except Track.DoesNotExist:
		raise Http404
	"""
	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography
	#return HttpResponse('Ok')
	return render(request, 'track.html', {'track': track, 'bio':bio})

def track_view_json(request, title):
	track = get_object_or_404(Track, title=title)
	bio = track.artist.biography

	data = {
		'title': track.title,
		'oder': track.order,
		'album': track.album.title,
		'artist': {
			'name': track.artist.first_name,
			'bio': bio
		}
	}

	json_data = json.dumps(data)
	#inverse: json.loads(string_json)

	return HttpResponse(json_data, content_type='application/json')