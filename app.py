# coding: utf-8
# email: khahux@163.com

from flask import Flask

from controllers.admin import admin
from controllers.index import index


def khahux_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_module(admin)
    app.register_module(index)

    return app
