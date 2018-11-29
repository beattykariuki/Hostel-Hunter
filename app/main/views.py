from flask import render_template
from . import main 

#Views
@main.route('/')
def index():

    '''
    Returns index page
    '''
    title = "HOME"
    return render_template('index.html', title=title)