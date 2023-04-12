from Website.models import Hospital
from flask import Blueprint,render_template,request,redirect,url_for
from .models import Hospital
from flask import render_template


home = Blueprint('home_page',__name__)

@home.route('/')
def home_func():
    if request.method == 'GET':
        return render_template('home.html', Hospitals = Hospital.query.all() )




