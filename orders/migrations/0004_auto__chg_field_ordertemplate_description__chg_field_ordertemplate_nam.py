# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'OrderTemplate.description'
        db.alter_column(u'orders_ordertemplate', 'description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'OrderTemplate.name'
        db.alter_column(u'orders_ordertemplate', 'name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'OrderTemplate.material'
        db.alter_column(u'orders_ordertemplate', 'material_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Material'], null=True))

        # Changing field 'OrderTemplate.color_front'
        db.alter_column(u'orders_ordertemplate', 'color_front_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['orders.Color']))

        # Changing field 'OrderTemplate.color_back'
        db.alter_column(u'orders_ordertemplate', 'color_back_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['orders.Color']))

        # Changing field 'OrderTemplate.lamination'
        db.alter_column(u'orders_ordertemplate', 'lamination_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Lamination'], null=True))

        # Changing field 'Orders.email'
        db.alter_column(u'orders_orders', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Orders.phone'
        db.alter_column(u'orders_orders', 'phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Orders.template'
        db.alter_column(u'orders_orders', 'template_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderTemplate'], unique=True, null=True))

        # Changing field 'Orders.FIO'
        db.alter_column(u'orders_orders', 'FIO', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.description'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.description' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.description'
        db.alter_column(u'orders_ordertemplate', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.name'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.name' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.name'
        db.alter_column(u'orders_ordertemplate', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.material'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.material' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.material'
        db.alter_column(u'orders_ordertemplate', 'material_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Material']))

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.color_front'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.color_front' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.color_front'
        db.alter_column(u'orders_ordertemplate', 'color_front_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Color']))

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.color_back'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.color_back' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.color_back'
        db.alter_column(u'orders_ordertemplate', 'color_back_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Color']))

        # User chose to not deal with backwards NULL issues for 'OrderTemplate.lamination'
        raise RuntimeError("Cannot reverse this migration. 'OrderTemplate.lamination' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'OrderTemplate.lamination'
        db.alter_column(u'orders_ordertemplate', 'lamination_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Lamination']))

        # User chose to not deal with backwards NULL issues for 'Orders.email'
        raise RuntimeError("Cannot reverse this migration. 'Orders.email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Orders.email'
        db.alter_column(u'orders_orders', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75))

        # User chose to not deal with backwards NULL issues for 'Orders.phone'
        raise RuntimeError("Cannot reverse this migration. 'Orders.phone' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Orders.phone'
        db.alter_column(u'orders_orders', 'phone', self.gf('django.db.models.fields.CharField')(max_length=255))

        # User chose to not deal with backwards NULL issues for 'Orders.template'
        raise RuntimeError("Cannot reverse this migration. 'Orders.template' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Orders.template'
        db.alter_column(u'orders_orders', 'template_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.OrderTemplate'], unique=True))

        # User chose to not deal with backwards NULL issues for 'Orders.FIO'
        raise RuntimeError("Cannot reverse this migration. 'Orders.FIO' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Orders.FIO'
        db.alter_column(u'orders_orders', 'FIO', self.gf('django.db.models.fields.CharField')(max_length=255))

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