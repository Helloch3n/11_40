from wtforms import Form, StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import data_required, InputRequired, Length, EqualTo
from apps.forms import BaseForm


class LoginForm(BaseForm):
    DL_ID = StringField(
        validators=[data_required(message='请输入工号'), InputRequired(message='请输入工号'), Length(6, message='请输入6位工号')])
    password = PasswordField(validators=[data_required('请输入密码'), Length(6, 20, message='请输入6-20位密码')])
    remember = IntegerField()
    submit = SubmitField()


class ResetpwdForm(BaseForm):
    oldpwd = PasswordField(validators=[data_required('请输入密码1'), Length(6, 20, message='请输入6-20位密码')])
    newpwd = PasswordField(validators=[data_required('请输入密码2'), Length(6, 20, message='请输入6-20位新密码')])
    newpwd2 = PasswordField(
        validators=[data_required('请输入密码3'), Length(6, 20, message='请输入6-20位新密码'),
                    EqualTo("newpwd", message="确认密码与新密码保持一致")])
