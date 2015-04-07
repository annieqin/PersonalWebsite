# coding: utf-8
# email: khahux@163.com

import datetime

from models.base import models, Model


class Films(Model):
    NO_TAGS = 0

    film_name = models.CharField(max_length=255, default='')
    film_url = models.CharField(max_length=255, default='')
    film_tags = models.IntegerField(default=NO_TAGS)

    created_at = models.DateTimeField(null=True, default=datetime.datetime.now)
    updated_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'films'