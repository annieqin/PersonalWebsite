# coding: utf-8
# email: khahux@163.com

from flask import Module, render_template, request, jsonify

from models.user import User
from forms.user import LoginForm

from base import status_message


admin = Module(__name__)


def return_status(status=599):
    return jsonify(status=status, message=status_message['status'])


# ---- 登录相关 -----
@admin.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('base_index.html')

    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            username = form.data.get('username', '')
            password = form.data.get('password', '')

            admin_user = User.authenticate(username, password)
            if admin_user:
                return_status(200)
            else:
                return_status(400)
        else:
            return_status(401)


@admin.route('/logout')
def logout():
    return render_template('base_index.html')


# ---- 后台相关 -----
@admin.route('/admin')
def khahux_admin():
    return render_template('a_blog.html')