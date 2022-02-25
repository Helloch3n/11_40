from exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class CMSUser(db.Model):
    __tablename__ = 'cms_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    DL_ID = db.Column(db.String(6), nullable=False, unique=True)
    join_time = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, username, password, DL_ID):
        self.username = username
        self.password = password
        self.DL_ID = DL_ID

    # 可以将一个类中的方法定义成属性
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw_password):
        self._password = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        result = check_password_hash(self.password, raw_password)
        return result

# 密码：对外的字段名叫做password，对内使用的字段名叫_password
