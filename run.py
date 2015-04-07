# coding: utf-8
# email: khahux@163.com

from app import khahux_app

from config import PORT


if __name__ == '__main__':
    app = khahux_app()
    app.run(port=PORT)