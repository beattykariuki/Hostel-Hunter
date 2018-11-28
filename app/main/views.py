from flask import render_template,redirect,url_for,abort
from app import create_app
from . import main

@main.route('/')
def search(uni_name):
    '''
    View function to display the search results
    '''
    uni_name_list= ['strathmore','Daystar']
    host_name_list=['Qwetu', 'Keri']

    uni_name_list = uni_name.split(" ")
    uni_name_format = "+".join(uni_name_list)
    searched_unis = search_uni(uni_name_format)
    title = f'search results for {uni_name}'
    return render_template('search.html',unis = searched_unis)
