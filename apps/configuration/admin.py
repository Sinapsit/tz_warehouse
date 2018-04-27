from django.contrib import admin
from solo.admin import SingletonModelAdmin
from configuration.models import RemoteServer

admin.site.register(RemoteServer, SingletonModelAdmin)