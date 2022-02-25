from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, \
    TextAreaField, TimeField, DateTimeField
from wtforms.validators import DataRequired, EqualTo, length
from .models import IT_SysRunSupportKind as IT_kind, IT_SysServiceType as IT_type, FrontUser
from flask import Blueprint
from sqlalchemy import create_engine
from flask import g
from exts import db
from config import DB_URI
from sqlalchemy.orm import sessionmaker


# 注册表单
class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), length(1, 16)], render_kw={'class': 'form-control'})
    DL_ID = StringField('工号', validators=[DataRequired(), length(6)], render_kw={'class': 'form-control'})
    password = PasswordField('密码', validators=[DataRequired(), length(8, 16)], render_kw={'class': 'form-control'})
    password_repeat = PasswordField('密码', validators=[DataRequired(), length(8, 16), EqualTo('password')],
                                    render_kw={'class': 'form-control'})
    submit = SubmitField('注册', render_kw={'class': 'btn btn-primary'})


class SearchForm(FlaskForm):
    search = StringField('搜索框', render_kw={'class': 'form-control me-2', 'placeholder': '别搜了，还用不了呢~'})
    submit = SubmitField('搜索一哈', render_kw={'class': 'btn btn-primary'})


# 登陆表单
class LoginForm(FlaskForm):
    DL_ID = StringField('用户名', validators=[DataRequired(), length(6, message='请输入6位工号')],
                        render_kw={'class': 'form-control'})
    password = PasswordField('密码', validators=[DataRequired(), length(8, 16, message='请输入6-20位密码')],
                             render_kw={'class': 'form-control'})
    remember = BooleanField('记住密码')
    submit = SubmitField('登录', render_kw={'class': 'btn btn-primary'})


# conn = engine.connect()
# sql = 'From '
# sql1 =
# conn.execute('')

# 查询服务类型和服务分类列表，在get请求里会有上下文
# for type in IT_type.query.with_entities(IT_type.service_type).all():
#     types = types + list(type)
#
# for name in IT_kind.query.with_entities(IT_kind.Name).all():
#     names = names + list(name)
engine = create_engine(DB_URI)
session = sessionmaker(engine)()


# 日志表单
class JournalForm(FlaskForm):
    types = ['--请选择--']
    names = ['--请选择--']
    for type in session.query(IT_type.service_type).all():
        types = types + list(type)
    for name in session.query(IT_kind.Name).all():
        names = names + list(name)

    service_type = SelectField('服务类型', validators=[DataRequired()], choices=types,
                               render_kw={'class': 'btn btn-primary dropdown-toggle dropdown-toggle-split'})

    start_time = TimeField('起始时间', validators=[DataRequired()], render_kw={'class': 'btn btn-primary'})

    service_classification = SelectField('服务分类', validators=[DataRequired()], choices=names,
                                         render_kw={
                                             'class': 'btn btn-primary dropdown-toggle dropdown-toggle-split'})

    # end_hours = TimeField('小时')
    end_time = TimeField('结束时间', validators=[DataRequired()], render_kw={'class': 'btn btn-primary'})
    hours = StringField('工时', validators=[DataRequired()], render_kw={'class': 'btn btn-primary'})
    problem_description = TextAreaField('问题描述', render_kw={'class': 'form-control'})
    cause_analysis = TextAreaField('原因分析', render_kw={'class': 'form-control'})
    process1 = TextAreaField('处理过程', render_kw={'class': 'form-control'})
    result = TextAreaField('处理结果', render_kw={'class': 'form-control'})
    submit = SubmitField('提交', render_kw={'class': 'btn btn-primary clearfix'})
