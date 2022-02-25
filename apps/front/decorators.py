from flask import session, redirect, url_for
from functools import wraps
import config


# 装饰器，判断是否登录，否则返回登陆页面
def login_required(func):
    @wraps(func)
    def inner(*args, **kwargs):
        if config.FRONT_USER_ID in session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('front.login'))

    return inner
