from flask import Blueprint, render_template, request

bp = Blueprint('maintain', __name__,
        template_folder='templates',
        static_folder='static')

@bp.route('/ping')
def ping():
    return 'pong'

@bp.route('/')
def index():
    return render_template('maintain_index.html', domain=request.url)
