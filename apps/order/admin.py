from django.contrib import admin
from order import models
from configuration.models import RemoteServer
from exchange.connector import BaseConnector


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'number',
        'created',
        'modified',
        'synced'
    ]

    readonly_fields = [
        'synced'
    ]

    def save_model(self, request, obj, form, change):
        """
        Given a model instance save it to the database.
        """
        obj.save()
        if form.changed_data and 'status' in form.changed_data:
            server = RemoteServer.get_solo()
            if server.url:
                connector = BaseConnector(obj.id, server.url)
                connector.sync_status()
