from Website.models import Hospital
from flask import Blueprint,render_template,request,redirect,url_for
from .models import Hospital
from flask import render_template


message = Blueprint('show_message',__name__)

@message.route('/display')
def msg():
    if request.method == 'GET':
        return render_template('message.html', Hospitals = Hospital.query.all())




