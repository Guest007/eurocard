# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Material'
        db.create_table(u'orders_material', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'orders', ['Material'])

        # Adding model 'Lamination'
        db.create_table(u'orders_lamination', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'orders', ['Lamination'])

        # Adding model 'Color'
        db.create_table(u'orders_color', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'orders', ['Color'])

        # Adding model 'OrderTemplate'
        db.create_table(u'orders_ordertemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('is_template', self.gf('django.db.models.fields.BooleanField')()),
            ('chip', self.gf('django.db.models.fields.BooleanField')()),
            ('scratch', self.gf('django.db.models.fields.BooleanField')()),
            ('magnet', self.gf('django.db.models.fields.BooleanField')()),
            ('emboss', self.gf('django.db.models.fields.BooleanField')()),
            ('uv', self.gf('django.db.models.fields.BooleanField')()),
            ('print_num', self.gf('django.db.models.fields.BooleanField')()),
            ('sign', self.gf('django.db.models.fields.BooleanField')()),
            ('foil', self.gf('django.db.models.fields.BooleanField')()),
            ('barcode', self.gf('django.db.models.fields.BooleanField')()),
            ('indent', self.gf('django.db.models.fields.BooleanField')()),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Material'])),
            ('lamination', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Lamination'])),
            ('color_front', self.gf('django.db.models.fields.related.ForeignKey')(related_name='color_front', to=orm['orders.Color'])),
            ('color_back', self.gf('django.db.models.fields.related.ForeignKey')(related_name='color_back', to=orm['orders.Color'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'orders', ['OrderTemplate'])

        # Adding model 'Orders'
        db.create_table(u'orders_orders', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('FIO', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('draw', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('maket', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('template', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.OrderTemplate'], unique=True)),
        ))
        db.send_create_signal(u'orders', ['Orders'])


    def backwards(self, orm):
        # Deleting model 'Material'
        db.delete_table(u'orders_material')

        # Deleting model 'Lamination'
        db.delete_table(u'orders_lamination')

        # Deleting model 'Color'
        db.delete_table(u'orders_color')

        # Deleting model 'OrderTemplate'
        db.delete_table(u'orders_ordertemplate')

        # Deleting model 'Orders'
        db.delete_table(u'orders_orders')


    models = {
        u'orders.color': {
            'Meta': {'object_name': 'Color'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.lamination': {
            'Meta': {'object_name': 'Lamination'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.material': {
            'Meta': {'object_name': 'Material'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'orders.orders': {
            'FIO': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'Orders'},
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maket': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['orders.OrderTemplate']", 'unique': 'True'})
        },
        u'orders.ordertemplate': {
            'Meta': {'object_name': 'OrderTemplate'},
            'barcode': ('django.db.models.fields.BooleanField', [], {}),
            'chip': ('django.db.models.fields.BooleanField', [], {}),
            'color_back': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'color_back'", 'to': u"orm['orders.Color']"}),
            'color_front': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'color_front'", 'to': u"orm['orders.Color']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'emboss': ('django.db.models.fields.BooleanField', [], {}),
            'foil': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'indent': ('django.db.models.fields.BooleanField', [], {}),
            'is_template': ('django.db.models.fields.BooleanField', [], {}),
            'lamination': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Lamination']"}),
            'magnet': ('django.db.models.fields.BooleanField', [], {}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Material']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'print_num': ('django.db.models.fields.BooleanField', [], {}),
            'scratch': ('django.db.models.fields.BooleanField', [], {}),
            'sign': ('django.db.models.fields.BooleanField', [], {}),
            'uv': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['orders']