# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Settings.is_richtext'
        db.delete_column(u'config_settings', 'is_richtext')

        # Adding field 'Settings.richtext'
        db.add_column(u'config_settings', 'richtext',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Settings.content'
        db.alter_column(u'config_settings', 'content', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):
        # Adding field 'Settings.is_richtext'
        db.add_column(u'config_settings', 'is_richtext',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Settings.richtext'
        db.delete_column(u'config_settings', 'richtext')


        # Changing field 'Settings.content'
        db.alter_column(u'config_settings', 'content', self.gf('django.db.models.fields.TextField')())

    models = {
        u'config.settings': {
            'Meta': {'object_name': 'Settings'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'richtext': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['config']