# coding: utf-8
# email: khahux@163.com

import datetime

from models.base import models, Model


class Resource(Model):
    NO_TAGS = 0

    resource_name = models.CharField(max_length=255, default='')
    resource_url = models.CharField(max_length=255, default='')
    resource_tags = models.IntegerField(default=NO_TAGS)

    created_at = models.DateTimeField(null=True, default=datetime.datetime.now)
    updated_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'resources'