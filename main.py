import random
import string
from firebase_admin import db , credentials
import firebase_admin
from datetime import datetime
import json
random_key = ''.join(random.choices(string.ascii_lowercase, k = 6))

import pyrebase

config = {
  "apiKey": "AIzaSyAlRWyTvQ7u64QUF2p4Lc-FHZipsTr4kYE",
  "authDomain": "mdd-fyp.firebaseapp.com",
  "databaseURL": "https://mdd-fyp-default-rtdb.firebaseio.com",
  "projectId": "mdd-fyp",
  "storageBucket": "mdd-fyp.appspot.com",
  "messagingSenderId": "228158034299",
  "appId": "1:228158034299:web:13753825314f684b842dde",
  "measurementId": "G-BGC3FNK5PW"
}

firebase = pyrebase.initialize_app(config)
from firebase_admin import auth as auths
dbs = firebase.database()
auth = firebase.auth()

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from cassandra_flask_sessions import  CassandraSessionInterface

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "secret"
CassandraSessionInterface(app)
cred = credentials.Certificate("C:/Users/Ebad/Downloads/mdd-fyp-firebase-adminsdk-rauyu-8afebf5f87.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://mdd-fyp-default-rtdb.firebaseio.com/'})

database = db.reference()


@app.route('/')
def landing_page():
    return render_template("landing_page.html")

@app.route('/login' , methods=['GET' , 'POST'])
def login():
    if request.method == 'POST':
        type_of_form = request.form.get("typee")
        if type_of_form == "signup":
            user_name = request.form['user_name']
            sign_up_mail = request.form['usermail']
            sign_up_pass = request.form['_password']
            user = auth.create_user_with_email_and_password(sign_up_mail,sign_up_pass)
            dbs.child('Users').update({user_name: user['localId']})
        elif type_of_form == "signin":
            user_email = request.form['username_']
            user_pass = request.form['password_']
            session['username_'] = request.form.get('username_')
            user = auth.sign_in_with_email_and_password(user_email,user_pass)
            session['username_'] = user
            auth.sign_in_with_email_and_password(user_email,user_pass)

    return render_template("login.html")

@app.route('/dashboard' , methods = ['GET' , 'POST'])
def dashboard():
    if 'username_' in session:
        email = session['username_']
        uid = email['localId']
        user_mail = auths.get_user(uid)
        emails = user_mail.email
        user_ref = database.child(uid)
        keys = user_ref.get()
        up = db.reference().get()
        if up is not None:
            for j in up:
                user_find = db.reference(j + '/user').get()
                if user_find is not None:
                    for i in user_find:
                        if i == uid:
                            val = db.reference(j + '/user').get()
                            value = val[uid]
                            hide_button = "<script>var gen_button = document.getElementById('genbutton').style.display = 'none';</script>"
                            hide_label = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
                            hide_entry = "<script>var gen_button = document.getElementById('gen__button').style.display = 'none';</script>"
                            hide_sub = "<script>var gen_button = document.getElementById('btn').style.display = 'none';</script>"
                            hide_label_or = "<script>var gen_button = document.getElementById('or').style.display = 'none';</script>"
                            hide_from_user = "<script>var gen_button = document.getElementById('hide_from_user').style.display = 'none';</script>"
                            msg = "Welcome", emails
                            msg_1 = "You are already registered into a Farm"
                            return render_template('dashboard.html', hide_button_script=hide_button, msg=msg_1,
                                                   hide=hide_label, hide_en=hide_entry, sub=hide_sub , hide_label_or = hide_label_or,
                                                   hide_from_user=hide_from_user)
                    else:
                        pass
                else:
                    pass

        if keys is not None:
            if request.method == 'POST':
                if request.form['gen'] == 'gen':
                    email = session['username_']
                    user_ids = email['localId']
                    key = random_key
                    dbs.child(user_ids).child('key').child(key).set(key)
            key_1 = db.reference(uid).get()
            key_val = key_1['key']
            val = key_val
            hide_label = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
            hide_entry = "<script>var gen_button = document.getElementById('gen__button').style.display = 'none';</script>"
            hide_sub = "<script>var gen_button = document.getElementById('btn').style.display = 'none';</script>"
            hide_label_or = "<script>var gen_button = document.getElementById('or').style.display = 'none';</script>"
            msg = "Your key is ", val
            counter_farm = db.reference(uid + '/key').get()
            count_farm = 0
            total_users = 0
            users_count = db.reference(uid + '/user').get()
            if users_count is None:
                pass
            else:
                for i in users_count:
                    total_users += 1
            for i in counter_farm:
                count_farm += 1
            farms_msg = 'Total farm you have: ', count_farm
            users_msg = 'Total users you have: ', total_users
            return render_template('dashboard.html', codes=msg, count_farm=farms_msg, hide=hide_label, hide_en=hide_entry,
                                   sub=hide_sub, users_total=users_msg , hide_label_or = hide_label_or)
            # if user_find is not None:
        #     for i in user_find:
        #         if i == uid:
        #           val = db.reference(key + '/key' ).get()
        #           hide_button =  "<script>var gen_button = document.getElementById('genbutton').style.display = 'none';</script>"
        #           hide_label = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
        #           hide_entry = "<script>var gen_button = document.getElementById('gen__button').style.display = 'none';</script>"
        #           hide_sub = "<script>var gen_button = document.getElementById('btn').style.display = 'none';</script>"
        #           msg = "Your key is " , val
        #         return render_template('home.html', hide_button_script=hide_button , codes = msg, hide = hide_label , hide_en = hide_entry, sub = hide_sub)
        else:
            try:
                if request.method == 'POST':
                    if request.form['subs'] == 'subs':
                        code = request.form['entry']
                        user_mail = session['username_']
                        user_id = user_mail['localId']
                        all_parents = db.reference()
                        parent_node = []
                        keys_node = []
                        is_present = all_parents.get()
                        for key in is_present:
                            parent_node.append(key)
                            for_sec_user = db.reference(key + '/key')
                            key_data = for_sec_user.get()
                            nodes_info = next(iter(key_data))
                            for i in key_data:
                                if i == code:
                                    dbs.child(key).child('user').update({user_id: i})

                    val = db.reference(key + '/user' + user_id).get()
                    hide_button = "<script>var gen_button = document.getElementById('genbutton').style.display = 'none';</script>"
                    hide_label = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
                    hide_entry = "<script>var gen_button = document.getElementById('gen__button').style.display = 'none';</script>"
                    hide_sub = "<script>var gen_button = document.getElementById('btn').style.display = 'none';</script>"
                    hide_label_or = "<script>var gen_button = document.getElementById('or').style.display = 'none';</script>"
                    hide_from_user = "<script>var gen_button = document.getElementById('hide_from_user').style.display = 'none';</script>"
                    msg_1 = "Your key is ", emails
                    msg = "You are already registered"
                    return render_template('dashboard.html', hide_button_script=hide_button, msg=msg, hide=hide_label,
                                           hide_en=hide_entry, sub=hide_sub ,hide_label_or=  hide_label_or, hide_from_user=hide_from_user)


            except:
                if request.method == 'POST':
                    if request.form['gen'] == 'gen':
                        email = session['username_']
                        user_ids = email['localId']
                        key = random_key
                        dbs.child(user_ids).child('key').child(key).set(key)
                key_1 = db.reference(uid).get()
                key_val = key_1['key']
                val = key_val
                hide_label = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
                hide_entry = "<script>var gen_button = document.getElementById('gen__button').style.display = 'none';</script>"
                hide_label_or = "<script>var gen_button = document.getElementById('gen_button').style.display = 'none';</script>"
                hide_sub = "<script>var gen_button = document.getElementById('btn').style.display = 'none';</script>"
                msg = "Your key is ", val

                return render_template('dashboard.html', codes=msg, hide=hide_label,
                                       hide_en=hide_entry, sub=hide_sub , hide_label_or= hide_label_or)
        return render_template('dashboard.html')

    if not session.get("username_"):
        return redirect(url_for('login'))
    else:
        return render_template('dashboard.html')

# @app.route('/admin_user')
# def admin_user():
#     if not session.get("username_"):
#         return redirect(url_for('login'))
#     else:
#         return render_template('admin_user.html')

@app.route('/user_manager')
def user_manager():
    if 'username_' in session:
        email = session['username_']
        uid = email['localId']
        user_mail = auths.get_user(uid)
        emails = user_mail.email
        user_ref = database.child(uid + '/key')
        keys = user_ref.get()
        # for key, value in keys.items():
        #     value['created_at'] = datetime.strptime(value['created_at'], '%Y-%m-%d %H:%M:%S.%f')
        # print(type(value['created_at']))
        farm_data = sorted(keys.items())

        user = database.child(uid + '/user').get()
        user_data = sorted(user.items())
    return render_template('user_manager.html', farm_key=farm_data , user_data = user_data)

if __name__ == "__main__":
    app.run(debug=True)