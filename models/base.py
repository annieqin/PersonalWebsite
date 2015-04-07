# coding: utf-8
# email: khahux@163.com

import peewee as models

from config import db_config


class Database(models.MySQLDatabase):
    pass


db = Database(**db_config)


class Model(models.Model):
    class Meta:
        database = db