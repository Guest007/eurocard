# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coefficient'
        db.create_table(u'orders_coefficient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('numb', self.gf('django.db.models.fields.IntegerField')()),
            ('coeff', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'orders', ['Coefficient'])

        # Adding field 'Lamination.cost'
        db.add_column(u'orders_lamination', 'cost',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Orders.cost'
        db.add_column(u'orders_orders', 'cost',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Orders.template'
        db.alter_column(u'orders_orders', 'template_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderTemplate'], unique=True))
        # Adding field 'Color.cost'
        db.add_column(u'orders_color', 'cost',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Material.cost'
        db.add_column(u'orders_material', 'cost',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Coefficient'
        db.delete_table(u'orders_coefficient')

        # Deleting field 'Lamination.cost'
        db.delete_column(u'orders_lamination', 'cost')

        # Deleting field 'Orders.cost'
        db.delete_column(u'orders_orders', 'cost')


        # Changing field 'Orders.template'
        db.alter_column(u'orders_orders', 'template_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['orders.OrderTemplate'], unique=True))
        # Deleting field 'Color.cost'
        db.delete_column(u'orders_color', 'cost')

        # Deleting field 'Material.cost'
        db.delete_column(u'orders_material', 'cost')


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
        u'orders.orders': {
            'FIO': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'Meta': {'object_name': 'Orders'},
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'draw': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maket': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.OrderTemplate']", 'unique': 'True'})
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