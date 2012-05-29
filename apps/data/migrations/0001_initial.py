# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Source'
        db.create_table('data_source', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal('data', ['Source'])

        # Adding model 'Fact'
        db.create_table('data_fact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Source'])),
            ('detail_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True)),
        ))
        db.send_create_signal('data', ['Fact'])

        # Adding model 'Rumor'
        db.create_table('data_rumor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('fact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Fact'], null=True)),
            ('keys', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('data', ['Rumor'])


    def backwards(self, orm):
        
        # Deleting model 'Source'
        db.delete_table('data_source')

        # Deleting model 'Fact'
        db.delete_table('data_fact')

        # Deleting model 'Rumor'
        db.delete_table('data_rumor')


    models = {
        'data.fact': {
            'Meta': {'object_name': 'Fact'},
            'detail_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Source']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        },
        'data.rumor': {
            'Meta': {'object_name': 'Rumor'},
            'fact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data.Fact']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keys': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        },
        'data.source': {
            'Meta': {'object_name': 'Source'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['data']
