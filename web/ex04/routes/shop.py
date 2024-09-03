from flask import Blueprint, render_template, request
from routes import dangun

bp = Blueprint('shop', __name__, url_prefix='/shop')

@bp.route('/search')
def search():
  return render_template(
    'index.html', title='상품검색', pageName='shop/search.html')


@bp.route('/search.json')
def searchJSON():
  args = request.args
  query = args['query']
  return dangun.search(query)

@bp.route('/list')
def list():
  return render_template(
    'index.html', title='상품목록', pageName='shop/list.html')

@bp.route('/read/<id>')
def read(id):
  return render_template(
    'index.html', title='상품정보', pageName='shop/read.html', id=id)
  