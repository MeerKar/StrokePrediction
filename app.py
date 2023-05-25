from flask import Flask, request, render_template, flash, jsonify
import pickle
from markupsafe import Markup

app = Flask(__name__)
app.secret_key = "apkofriowjfkf"
@app.route("/")
def index():
    return render_template('index_1.html')
@app.route("/output",methods=["POST","GET"])
#user-input
def output():
    if request.method == 'POST':
        #gender
        g = request.form['gender']
        if g == "male":
            g = 1
        elif g == "female":
            g = 0
        else:
            g = 2
        #age
        a = request.form['age']
        a = int(a)
        a = ((a-0.08)/(82-0.08))
        #hyper-tension
        hyt = request.form['hypertension']
        hyt = hyt.lower()
        if hyt == "yes":
            hyt = 1
        else:
            hyt = 0
        #heart-disease
        ht = request.form['heart-disease']
        ht = ht.lower()
        if ht == "yes":
            ht = 1
        else:
            ht = 0
        #marriage
        m = request.form['marriage']
        m = m.lower()
        if m == "yes":
            m = 1
        else:
            m = 0
        #worktype
        w = request.form['worktype']
        w = w.lower()
        if w == "government":
            w = 0
        elif w == "student":
            w = 1
        elif w == "private":
            w = 2
        elif w == "self-employed":
            w = 3
        else:
            w = 4
        #residency-type
        r = request.form['residency']
        r = r.lower()
        if r == "urban":
            r = 1
        elif r == 'rural':
            r = 2
        else: 
            r=0
        #glucose-levels
        gl = request.form['glucose']
        gl = int(gl)
        gl =  ((int(gl) - 55)/(271 - 55))
        #bmi
        b = request.form['bmi']
        b = int(b)
        b = ((b-10.3)/(97.6-10.3))
        #smoking
        s = request.form['smoking']
        if s == "unknown":
            s = 0
        elif s == "never smoked":
            s = 1
        elif s == "formerly smoked":
            s = 2
        elif s == "smokes":
            s = 3
        else:
            s = 0
        try:
            prediction = stroke_pred(g,a,hyt,ht,m,w,r,gl,b,s)
            return render_template('index_2.html',prediction_html=prediction)
        except ValueError:
            return "Please Enter Valid Values"
#prediction-model
def stroke_pred(g,a,hyt,ht,m,w,r,gl,b,s):
    #load model
    # model = pickle.load(open('model.pkl','rb'))
    with open('model/model.pkl', 'rb') as f: 
        model=pickle.load(f)
    #predictions
    user_input=(g,a,hyt,ht,m,w,r,gl,b,s)
    print(user_input)
    print('hello world')
    decoded_user_input=fancy_deconstruct(user_input)
    print(decoded_user_input)
    result = model.predict([decoded_user_input])
    print(result)
     #output
    if result == 1:
        return Markup("Patient is at risk of stroke. <br> Please provide recommendations for managing and reducing the risk of stroke. Consider lifestyle modifications, preventive measures, and any other relevant advice to improve the patient's overall health and minimize the risk of stroke.")
    elif result == 0:
        return  Markup("No risk of stroke detected. <br> Please continue monitoring patient's health and well-being. Kindly offer recommendations to maintain their overall health, taking into account lifestyle factors, preventive measures, and any other relevant advice that can contribute to their well-being.")
    else:
        return "A problem has occured in processing your data. Try again."
    
def fancy_deconstruct(user_input): 
    g,a,hyt,ht,m,w,r,gl,b,s=user_input
    g_female, g_male=(0, 0)
    if g==0: 
        g_female=1
    else: 
        g_male=1

    m_yes, m_no=(0, 0)
    if m==1: 
        m_yes=1
    else:
        m_no=0

    w_children, w_self, w_private, w_never, w_gov=(0, 0, 0, 0, 0)
    if w==4:  
        w_children=1
    elif w==3: 
        w_self=1
    elif w==2:
        w_private=1
    elif w==1:
        w_never=1
    else: 
        w_gov=1

    r_urban, r_rural, r_unknown=(0, 0, 0)
    if r==1:
        r_urban=1
    elif r==2: 
        r_rural=1
    else: 
        r_unknown=1

    s_unknown, s_never, s_former, s_yes=(0, 0, 0, 0)
    if s==0: 
        s_unknown=1
    elif s==1: 
        s_never=1
    elif s==2:
        s_former=1
    else: 
        s_yes=1

    decoded_input=[a, hyt, ht, gl, b, g_female, g_male, m_no, m_yes, w_gov, w_never, w_private, w_self, w_children, 
              r_rural, r_urban, s_unknown, s_former, s_never, s_yes]
    return decoded_input


if __name__=='__main__': 
	app.run()