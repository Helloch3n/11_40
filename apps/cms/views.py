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
from .forms import LoginForm, ResetpwdForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db

# 创建蓝图，指定子域名
# cms_bp = Blueprint('cms', __name__, subdomain='css')
cms_bp = Blueprint('cms', __name__, url_prefix='/cms')


@cms_bp.route('/')
@login_required
def index():
    # g.cms_user
    return render_template('cms/cms_index.html')


@cms_bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    # session.clear()
    return redirect(url_for('cms.login'))


@cms_bp.route('/profile/')
@login_required
def profile():
    return render_template('cms/cms_profile.html')


class LoginView(views.MethodView):
    def get(self, message=None):
        # flash(message)
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            DL_ID = form.DL_ID.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(DL_ID=DL_ID).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 如果设置记住我，session.permanent = True
                    # 那么cookie过期时间31天
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message='工号或者密码错误')
        else:
            print(form.errors)
            # ('password',['请输入6-20位密码'])
            message = form.get_error()
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetpwd.html')

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # ("code":200,message="密码错误")
                return jsonify({"code": 200, "message": ""})
            else:
                return jsonify({"code": 400, "message": "旧密码错误"})

        else:
            message = form.get_error()
            print(message)
            return jsonify({"code": 400, "message": message})


cms_bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
cms_bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
