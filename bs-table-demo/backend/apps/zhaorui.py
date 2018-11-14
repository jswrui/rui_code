from flask import Blueprint
from flask import render_template, url_for

from .. import env

# print(__name__.split('.')[-1])

bp = Blueprint(
    __name__,
    __name__,
    template_folder=env.DIR_TEMPLATES,
    static_folder=env.DIR_STATIC
)

@bp.route('/')
def view_index():
    return render_template('zhaorui/table-demo.html')