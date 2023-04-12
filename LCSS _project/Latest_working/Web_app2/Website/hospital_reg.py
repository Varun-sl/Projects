from flask import Blueprint,render_template,request,redirect,url_for
from .models import Hospital
from . import db

hospital_reg = Blueprint('hospital_registration',__name__)

@hospital_reg.route('/hospital_registration', methods = ['GET','POST'])
def registration():
    
    if request.method == 'POST':
        print("inside home POST method")
        hospital_name = request.form.get('hospital_name')
        location = request.form.get('location')
        no_of_beds = request.form.get('no_of_beds')

        hospital = Hospital(hospital_name = hospital_name, location = location, beds = no_of_beds)
        db.session.add(hospital)
        db.session.commit()

        return redirect(url_for('home_page.home_func'))
        

    if request.method == 'GET':
        print("inside home GET method")
        return render_template("hospital_reg.html")
