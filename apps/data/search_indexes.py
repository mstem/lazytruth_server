
import datetime
from haystack.indexes import *
from haystack import site
from lazytruth.apps.data.models import Rumor


class RumorIndex(SearchIndex):
    title = CharField()
    text = CharField(document=True)
    keys = CharField()#db_index=True
    def index_queryset(self):
        return Rumor.objects.all()


site.register(Rumor, RumorIndex)