from .views import front_bp
# from .journal_views import journal_bp
from flask import g, session
import config
from .models import FrontUser


@front_bp.before_request
def before_request():
    # 判断用户是否登录
    if config.FRONT_USER_ID in session:
        # print(config.FRONT_USER_ID)
        # 在session中查找用户id
        user_id = session.get(config.FRONT_USER_ID)
        # print(user_id)
        # 根据用户id在数据库中查找用户对象
        user = FrontUser.query.get(user_id)
        if user:
            # 将用户对象变为全局变量
            g.front_user = user

# @journal_bp.before_request
# def before_request():
#     if config.FRONT_USER_ID in session:
#         print(config.FRONT_USER_ID)
#         user_id = session.get(config.FRONT_USER_ID)
#         print(user_id)
#         user = FrontUser.query.get(user_id)
#         if user:
#             g.front_user = user
