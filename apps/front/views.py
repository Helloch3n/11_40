from flask import (Blueprint,
                   views,
                   render_template,
                   request,
                   session,
                   redirect,
                   url_for,
                   flash,
                   g,
                   jsonify)
from .forms import RegisterForm, LoginForm, SearchForm, JournalForm
import config
from exts import db
from .models import FrontUser, IT_SysRunSupportKind as IT_kind, IT_SysRunSupport as IT_support, \
    IT_SysServiceType as IT_type
from .decorators import login_required
from sqlalchemy import create_engine
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField, TextAreaField
from wtforms.validators import DataRequired

# 创建蓝图，指定子域名
front_bp = Blueprint('front', __name__)


# 主页面
@front_bp.route('/')
@login_required
def index():
    form = SearchForm()
    return render_template('front/front_index.html', form=form)


# 作者简介
@front_bp.route('/itta/')
@login_required
def itta():
    return render_template('front/front_Introduction_to_the_author.html')


# 注销
@front_bp.route('/logout/')
@login_required
def logout():
    del session[config.FRONT_USER_ID]
    # session.clear()
    return redirect(url_for('front.login'))


# 日志
@front_bp.route('/write/', methods=['GET', 'POST'])
@login_required
def write():
    # types = ['--请选择--']
    # names = ['--请选择--']
    # # 查询服务类型和服务分类列表，在get请求里会有上下文
    # for type in IT_type.query.with_entities(IT_type.service_type).all():
    #     types = types + list(type)
    #
    # for name in IT_kind.query.with_entities(IT_kind.Name).all():
    #     names = names + list(name)
    # print(types)
    # print(names)
    form = JournalForm()
    if form.submit.data and form.validate_on_submit():
        NeederId = ''
        NeedTime = datetime.now()
        Type = IT_kind.query.with_entities(IT_kind.Type).filter_by(Name=form.service_classification.data).first()[0]
        Kind = IT_kind.query.with_entities(IT_kind.Id).filter_by(Name=form.service_classification.data).first()[0]
        Sys = 0
        Part = 0
        NeedDesc = form.problem_description.data
        Reson = form.cause_analysis.data
        Process = form.process1.data
        Result = form.result.data
        BeginTime = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')}" + f" {form.start_time.data}",
                                      "%Y-%m-%d %H:%M:%S")
        EndTime = datetime.strptime(f"{datetime.now().strftime('%Y-%m-%d')}" + f" {form.end_time.data}",
                                    "%Y-%m-%d %H:%M:%S")
        WorkHours = form.hours.data
        DealerId = 'A1'
        Dealers = g.front_user.username
        Tool = 0
        journal = IT_support(NeederId, NeedTime, Type, Kind, Sys, Part,
                             NeedDesc, Reson, Process, Result, BeginTime, EndTime, WorkHours,
                             DealerId, Dealers, Tool)
        db.session.add(journal)
        db.session.commit()
        flash('提交成功')
        return redirect(url_for('front.write'))
    elif request.method == 'POST':
        # 调用ajax.js
        data = request.get_json()
        name = data['name']

        class_ = []
        # 子查询找到服务类型对应的服务分类
        id = IT_type.query.with_entities(IT_type.id).filter(IT_type.service_type == name).all()[0][0]
        for cls in IT_kind.query.with_entities(IT_kind.Name).filter(IT_kind.Type == id).all():
            class_ = list(cls) + class_
        return jsonify(class_)
    return render_template('front/front_journal_write.html', form=form)


# 个人中心
@front_bp.route('/profile/')
@login_required
def profile():
    return render_template('front/front_user_base.html')


# 登录
class LoginView(views.MethodView):
    def __init__(self):
        self.form = LoginForm()

    def get(self, message=None):
        # flash(message)
        return render_template('front/front_login.html', message=message, form=self.form)

    def post(self):
        # form = LoginForm(request.form)

        if self.form.validate_on_submit():
            DL_ID = self.form.DL_ID.data
            password = self.form.password.data
            remember = self.form.remember.data
            user = FrontUser.query.filter_by(DL_ID=DL_ID).first()
            # print(user.username)
            if user and user.check_password(password):
                session[config.FRONT_USER_ID] = user.id
                if remember:
                    # 如果设置记住我，session.permanent = True
                    # 那么cookie过期时间31天
                    session.permanent = True
                return redirect(url_for('front.index'))
            else:
                return self.get(message='工号或者密码错误')
        # else:
        #     print(self.form.errors)
        #     # ('password',['请输入6-20位密码'])
        #     message = self.form.get_error()
        #     return self.get(message=message)


# 注册
class RegView(views.MethodView):
    def __init__(self):
        self.form = RegisterForm()

    def get(self, message=None):
        return render_template('front/front_reg.html', message=message, form=self.form)

    def post(self):
        if self.form.validate_on_submit():
            username = self.form.username.data
            DL_ID = self.form.DL_ID.data
            password = self.form.password.data
            # 校验账号是否存在
            if FrontUser.query.filter(FrontUser.DL_ID == DL_ID):
                return self.get(message='此工号已经存在')
            else:
                user = FrontUser(DL_ID=DL_ID, username=username, password=password)
                db.session.add(user)
                db.session.commit()
        return redirect(url_for('front.login'))


front_bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
front_bp.add_url_rule('/reg/', view_func=RegView.as_view('reg'))
