# coding: utf-8
# email: khahux@163.com

import datetime

from models.base import models, Model


class Notes(Model):
    NO_TAGS = 0

    note_title = models.CharField(max_length=20, default='')
    note_content = models.TextField(default='')
    note_tags = models.IntegerField(default=NO_TAGS)

    created_at = models.DateTimeField(null=True, default=datetime.datetime.now)
    updated_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'notes'