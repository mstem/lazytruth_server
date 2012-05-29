from apps.data.keys import hashpipe
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from apps.data.models import Rumor
import json,IPython

@csrf_exempt
def match(request):

	print request.POST
	if 'text' not in request.POST:
		if 'body' in request.POST:
			text = json.loads(request.POST['body'])['text']
		else:
			try:
				text = json.loads(request.POST.keys()[0])['text']
			except:
				x = dict(request.POST)
				a = x.keys()[0]
				text = json.loads(a.replace('""','"'))['text']

				#return HttpResponse(json.dumps(dict(error="No data to check")))
	else:
		text = request.POST['text']
	print 'New Request:\n\t',text.strip()
	keys =  hashpipe.get_keys(text)
	nowhitespaceplain = keys.pop('nowhitespaceplain')
	print 'Number of non-whitespace characters',len(nowhitespaceplain),'\nLookup Keys',keys,nowhitespaceplain
	[a,b] = keys.values()
	#don't want false positives so asserting a min length on plain text contains
	len_nwp = len(nowhitespaceplain)

	if len_nwp > 500:
		alt = nowhitespaceplain[265:len_nwp-150]
		filters = Q(keys__contains=a) | Q(keys__contains=b) | Q(keys__contains=nowhitespaceplain) | Q(keys__contains=alt) 
	elif len_nwp > 400:
		alt = nowhitespaceplain[165:len_nwp-150]
		filters = Q(keys__contains=a) | Q(keys__contains=b) | Q(keys__contains=nowhitespaceplain) | Q(keys__contains=alt) 
	else:
		filters = Q(keys__contains=a) | Q(keys__contains=b)
	rumors = Rumor.objects.filter(
		filters,
		fact__isnull=False, 
	)
	#IPython.embed()
	if rumors.count() > 0:
		data = rumors[0].export()
		print 'Match found'
	else:
		data = dict(matched = False)
		print 'No match found'
		#IPython.embed()Rumor
	print json.dumps(data)
	response = HttpResponse(json.dumps(data))	
	#sresponse['Access-Control-Allow-Origin'] = '*'
	return response


@csrf_exempt
def post_mirror(request):
	response = HttpResponse(json.dumps(dict(request.POST)))	
	return response

def test(request):
	return render_to_response('test_api.html', {'version': settings.API_VERSION})
