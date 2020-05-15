from flask import Blueprint, render_template, request

bp = Blueprint('maintain', __name__,
        template_folder='templates',
        static_folder='static')

@bp.route('/ping')
def maintain_ping():
    return 'pong'

@bp.route('/')
def maintain_index():
    return render_template('maintain_index.html', domain=request.url)

@bp.route('/test')
def test():
    return render_template('test.html')
