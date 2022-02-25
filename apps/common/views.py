from flask import Blueprint

# 创建蓝图，指定子域名
# cms_bp = Blueprint('cms', __name__, subdomain='css')
common_bp = Blueprint('common', __name__, url_prefix='/common')


@common_bp.route('/')
def index():
    return 'common index'
