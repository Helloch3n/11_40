# config.py存放app配置文件

import os

# 设置secret_key，重启服务器后会重置secret_key导致session、cookie失效
SECRET_KEY = os.urandom(24)

# 设置debug模式
DEBUG = True

# 设置W_11数据库URI
DB_USERNAME = 'dlxxl'
DB_PASSWORD = 'Lrc123456'
DB_HOST = '10.40.10.10'
DB_NAME = 'W_11'
# 'mssql+pymssql://dlxxl:Lrc123456@10.40.10.10/TestLrc2'
DB_URI = "mssql+pymssql://{username}:{password}@{host}/{dbname}?charset=utf8".format(username=DB_USERNAME,
                                                                                     password=DB_PASSWORD,
                                                                                     host=DB_HOST, dbname=DB_NAME)

# 设置NEW_DLXX1数据库URI
DB_USERNAME1 = 'dlxxl'
DB_PASSWORD1 = 'Lrc123456'
DB_HOST1 = '10.40.10.10'
DB_NAME1 = 'NEW_DLXX1'
# 'mssql+pymssql://dlxxl:Lrc123456@10.40.10.10/TestLrc2'
DB_URI_1 = "mssql+pymssql://{username}:{password}@{host}/{dbname}?charset=utf8".format(username=DB_USERNAME,
                                                                                       password=DB_PASSWORD,
                                                                                       host=DB_HOST, dbname=DB_NAME)
# 设置DLXX数据库URI
DB_USERNAME2 = 'dlxxl'
DB_PASSWORD2 = 'Lrc123456'
DB_HOST2 = '10.40.10.10'
DB_NAME2 = 'DLXX'
# 'mssql+pymssql://dlxxl:Lrc123456@10.40.10.10/TestLrc2'
DB_URI_2 = "mssql+pymssql://{username}:{password}@{host}/{dbname}?charset=utf8".format(username=DB_USERNAME,
                                                                                       password=DB_PASSWORD,
                                                                                       host=DB_HOST, dbname=DB_NAME)

# 设置URI
SQLALCHEMY_DATABASE_URI = DB_URI
# 设置多URI
SQLALCHEMY_BINDS = {'NEW_DLXX1': DB_URI_1, 'DLXX': DB_URI_2}
# 关闭Flask-SQLAlchemy事件系统（并禁用警告）
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 更改cookie过期失效
# PERMANENT_SESSION_LIEFTIME = timedelta(days=15)

# 设置cokkie id
CMS_USER_ID = 'WULAWALA'

FRONT_USER_ID = 'YIXIHAHA'
