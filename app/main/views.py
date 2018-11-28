from flask import render_template,redirect,url_for,abort,request
from .forms import SearchForm
from ..models import University
from app import create_app
from . import main
from .. import db
from flask import flash

# init_db()
@main.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@main.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = db_session.query(Hostel)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
# display results
    else:
        return render_template('results.html', results=results)



if __name__ == '__main__':
    app.run()