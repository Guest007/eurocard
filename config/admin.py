# -*- coding: utf-8 -*-
from django.contrib import admin
from config.models import Settings


class SettingsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'description']

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup/config_setup.js',
        )

admin.site.register(Settings, SettingsAdmin)
