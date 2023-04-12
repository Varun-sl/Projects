from Website.models import Hospital
from flask import Blueprint,render_template,request,redirect,url_for
from .models import Hospital
from flask import render_template
from . import db


info = Blueprint('info_page',__name__)
register = Blueprint('register_page',__name__)

@info.route('/info/<hospital_id>', methods = ['GET','POST'])
def information(hospital_id):
    hospital_id == request.view_args['hospital_id']
    if request.method == 'POST':
        print("inside post function")
        print(hospital_id)
        h = Hospital.query.get(hospital_id)
        print("No of beds = ")
        print(h.beds)
        if h.beds>0:
            h.beds = h.beds-1
        db.session.commit()
        return redirect(url_for('show_message.msg'))
    if request.method == 'GET':
        print(hospital_id)
        return render_template('user_info.html', hospital_id = hospital_id )




