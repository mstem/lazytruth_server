from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from apps.data.keys import hashpipe
import json

class Source(models.Model):
    url = models.URLField(max_length=250)
    name = models.CharField(max_length=250)
    icon = models.ImageField(upload_to='sourceicons',null=True,blank=True)
    def __unicode__(self):
    	return "%s, %s" % (self.name,self.url)

class Fact(models.Model):
    title = models.CharField(max_length=250,null=True)
    source = models.ForeignKey(Source)
    detail_url = models.URLField(null=True,max_length=250,blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='factimages',null=True,blank=True)
    def __unicode__(self):
    	return self.title if self.title != None else self.text.split('/n').pop(0)[:50]
    
class Rumor(models.Model):
    title = models.CharField(max_length=250,null=True,blank=True)
    text = models.TextField()
    fact = models.ForeignKey(Fact,null=True)
    keys = models.TextField()#db_index=True
    def __unicode__(self):
    	return "%s >> %s" % ( self.title if self.title != None else self.text.split('/n').pop(0)[:50], unicode(self.fact))
    def save(self, *args, **kwargs):
        self.keys = json.dumps(hashpipe.get_keys(self.text))
        super(Rumor, self).save(*args, **kwargs)
    def export(self):
        if self.fact != None:
            fact = self.fact
            source = fact.source
            data = dict(
                matched = True,
                fact_title = fact.title,
                fact_text = fact.text,
                fact_image_url = fact.image.url if fact.image else None,
                source_name = source.name,
                source_url = source.url,
                source_icon_url = source.icon.url if source.icon else None,
                detail_url = fact.detail_url,
            )
        else:
            data = dict(matched = False)
        return data