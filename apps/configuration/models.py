from django.db import models
from solo.models import SingletonModel


class RemoteServer(SingletonModel):
    url = models.URLField(blank=True, null=True, default=None)

    def __str__(self):
        return u"Remote Server"

    class Meta:
        verbose_name = "Remote Server"
