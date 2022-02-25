# 主app文件，创建app，设置错误处理视图，导入蓝图，设置csrf保护，连接数据库db

    from flask import Flask, render_template
from apps.cms.views import cms_bp
from apps.common.views import common_bp
from apps.front.views import front_bp
import config
from exts import db
from flask_wtf import CSRFProtect
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)

    # 因为在exts中使用db = SQLAlchemy()没有传入app做参数，所有要做此步骤
    db.init_app(app)
    # Migrate绑定数据库迁移
    Migrate(app, db)
    # CSRF保护
    CSRFProtect(app)

    # 404 错误处理器
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('front/front_404.html'), 404

    # 500 错误处理器
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('front/front_500.html'), 500

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=80)
