# coding: utf-8
# email: khahux@163.com

import hashlib

from lib.utils import random_string
from models.base import models, Model


class User(Model):
    username = models.CharField(max_length=20, default='')
    email = models.CharField(max_length=64, default='')

    password_hash = models.CharField(max_length=64, default='')
    password_salt = models.CharField(max_length=8, default='')

    last_login_at = models.DateTimeField(null=True, default=None)
    last_login_ip = models.CharField(max_length=15, default='')

    class Meta:
        db_table = 'user'

    def encrypt_password(self, password, salt=None):
        if not salt:
            salt = self.password_salt or self.regenerate_salt()
        return hashlib.sha256('{password} - {salt}'.format(password=password, salt=salt)).hexdigest()

    def regenerate_salt(self):
        self.password_salt = random_string(8)
        return self.password_salt

    def set_password(self, password):
        self.password_hash = self.encrypt_password(password)

    def verify_password(self, password):
        return self.encrypt_password(password) == self.password_hash

    def authenticate(self, username, password):
        try:
            user = User.get(
                User.username == username,
            )

            if not user.verify_password(password):
                user = None
        except User.DoesNotExist:
            user = None

        return user