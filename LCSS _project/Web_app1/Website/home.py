from Website.models import Hospital
from flask import Blueprint,render_template,request
from .models import Hospital
from flask import Flask, flash, url_for, redirect, render_template
from flask_sqlalchemy import  SQLAlchemy


home = Blueprint('home_page',__name__)

@home.route('/')
def home_func():
    return render_template('home.html', Hospitals = Hospital.query.all() )

    #return "<h1>This is TABLE</h1>"



