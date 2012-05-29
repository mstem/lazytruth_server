from django.core.management.base import BaseCommand, CommandError
import os.path,csv
import IPython
from apps.data.models import Source,Fact,Rumor
class Command(BaseCommand):
    help = 'Imports the google doc data Matt aquired'

    def handle(self, *args, **options):
		data_file = open(os.path.abspath('sourcedata/via_matt.csv'))
		rows = list(csv.DictReader(data_file))
		for row in rows:
			print row
			try:
				domain = row['Debunk URL'].split('/').pop(2)
			except:
				domain = 'unknown.com'
			source,toss = Source.objects.get_or_create(
				url = 'http://%s' % domain,
				name = domain,
			)
			fact,toss = Fact.objects.get_or_create(
				title = row['Email'].split('Fw:').pop(1).split('\n').pop(0) if 'Fw:' in row['Email'] else None,
				source = source,
				detail_url = row['Debunk URL'],
				text = row['Debunk'],
			)
			rumor,toss = Rumor.objects.get_or_create(
				text = row['Email'].decode('utf-8','replace'),
				fact = fact
			)
#IPython.embed()












