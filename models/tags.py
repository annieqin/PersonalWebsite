# coding: utf-8
# email: khahux@163.com

import datetime

from models.base import models, Model


class Tags(Model):
    NORMAL = 0
    BLOG_TAG = 1
    NOTE_TAG = 2
    RESOURCE_TAG = 3
    BOOK_TAG = 4
    FILM_TAG = 5

    tag = models.CharField(max_length=20, default='')
    belong = models.IntegerField(default=0)

    created_at = models.DateTimeField(null=True, default=datetime.datetime.now)
    updated_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'tags'