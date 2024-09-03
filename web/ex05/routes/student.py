from flask import Blueprint, render_template, request

bp = Blueprint('student' ,__name__, url_prefix='/student')

@bp.route('/search')
def search():
    return render_template('index.html',title='학생검색', pageName='student/search.html')


