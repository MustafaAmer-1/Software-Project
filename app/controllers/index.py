from flask import Blueprint ,  render_template

index_manage = Blueprint('index_manage', __name__)


@index_manage.route("/")
def index():
    return render_template('index.html') 

