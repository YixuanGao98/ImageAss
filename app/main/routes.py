from flask import render_template
from flask_login import login_required
from app.models import User
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
	return render_template('main/index.html', title='Hello')


@bp.route('/about')
def about():
	return render_template('main/about.html', title='About')
