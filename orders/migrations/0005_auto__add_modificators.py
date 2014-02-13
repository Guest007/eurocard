# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Modificators'
        db.create_table(u'orders_modificators', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cost', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'orders', ['Modificators'])


    def backwards(self, orm):
        # Deleting model 'Modificators'
        db.delete_table(u'orders_modificators')


    models = {
        u'orders.coefficient': {
            'Meta': {'object_name': 'Coefficient'},
            'coeff': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numb': ('django.db.models.fields.IntegerField', [], {})
        },
        u'orders.color': {
            'Meta': {'object_name': 'Color'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.lamination': {
            'Meta': {'object_name': 'Lamination'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.material': {
            'Meta': {'object_name': 'Material'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.modificators': {
            'Meta': {'object_name': 'Modificators'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'orders.orders': {
            'FIO': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Orders'},
            'cost': ('django.db.models.fields.FloatField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maket': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.OrderTemplate']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'orders.ordertemplate': {
            'Meta': {'object_name': 'OrderTemplate'},
            'barcode': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'chip': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'color_back': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'color_back'", 'null': 'True', 'to': u"orm['orders.Color']"}),
            'color_front': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'color_front'", 'null': 'True', 'to': u"orm['orders.Color']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'emboss': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'foil': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'indent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_template': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'lamination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Lamination']", 'null': 'True', 'blank': 'True'}),
            'magnet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Material']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'print_num': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'scratch': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sign': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uv': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['orders']