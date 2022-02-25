from exts import db
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# 用户注册
class FrontUser(db.Model):
    __tabelname__ = 'front_user'
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    DL_ID = db.Column(db.String(6), nullable=False, unique=True)
    username = db.Column(db.String(50), nullable=False)
    _password = db.Column(db.String(200), nullable=False)
    # 头像
    avatar = db.Column(db.String(100))
    join_time = db.Column(db.DateTime, default=datetime.now)

    # def __init__(self, *args, **kwargs):
    #     if "password" in kwargs:
    #         self.password = kwargs.get('password')
    #         kwargs.pop("password")
    #     super(FrontUser, self).__init__(*args, **kwargs)

    def __init__(self, DL_ID, username, password):
        self.DL_ID = DL_ID
        self.username = username
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, newpwd):
        self._password = generate_password_hash(newpwd)

    def check_password(self, rawpwd):
        # print(generate_password_hash(rawpwd))
        # print(check_password_hash(self._password, rawpwd))
        return check_password_hash(self._password, rawpwd)


# 日志数据库模型
class IT_SysRunSupport(db.Model):
    # __bind_key__ = 'DLXX'
    __tablename__ = 'IT_SysRunSupport'
    Id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    NeederId = db.Column(db.String(8), nullable=True)
    NeedTime = db.Column(db.DateTime, default=datetime.now)
    Type = db.Column(db.Integer)
    Kind = db.Column(db.String(3))
    Sys = db.Column(db.Integer)
    Part = db.Column(db.Integer)
    NeedDesc = db.Column(db.String(200))
    Reson = db.Column(db.String(100))
    Process = db.Column(db.String(200))
    Result = db.Column(db.String(50))
    BeginTime = db.Column(db.DateTime)
    EndTime = db.Column(db.DateTime)
    WorkHours = db.Column(db.DECIMAL(5, 2))
    DealerId = db.Column(db.String(2))
    Dealers = db.Column(db.String(20))
    Tool = db.Column(db.Integer)

    # RegDate = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, NeederId, NeedTime, Type, Kind, Sys, Part, NeedDesc, Reson, Process, Result,
                 BeginTime, EndTime, WorkHours, DealerId, Dealers, Tool):
        # self.Id = Id
        self.NeederId = NeederId
        self.NeedTime = NeedTime
        self.Kind = Kind
        self.Type = Type
        self.Sys = Sys
        self.Part = Part
        self.NeedDesc = NeedDesc
        self.Reson = Reson
        self.Process = Process
        self.Result = Result
        self.BeginTime = BeginTime
        self.EndTime = EndTime
        self.DealerId = DealerId
        self.Dealers = Dealers
        self.Tool = Tool
        # self.RegDate = RegDate
        self.WorkHours = WorkHours


# 服务分类数
class IT_SysRunSupportKind(db.Model):
    # __bind_key__ = 'DLXX'
    __tablename__ = 'IT_SysRunSupportKind'
    Id = db.Column(db.String(3), primary_key=True)
    Name = db.Column(db.String(16))
    Type = db.Column(db.Integer)
    Hours = db.Column(db.DECIMAL(5, 2))

    # CopyHours = db.Column(db.Boolean)

    def __init__(self, Id, Name, Type, Hours):
        self.Id = Id
        self.Name = Name
        self.Type = Type
        self.Hours = Hours
        # self.CopyHours = CopyHours


# 服务类型数据库模型
class IT_SysServiceType(db.Model):
    # __bind_key__ = 'DLXX'
    __tablename__ = 'IT_SysServiceType'
    id = db.Column(db.Integer, primary_key=True)
    service_type = db.Column(db.String(50))

    def __init__(self, id, service_type):
        self.id = id
        self.service_type = service_type
