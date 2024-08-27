import numpy as np
import model
from flask import Flask, request, render_template
import pickle
import model1
app = Flask(__name__,template_folder="templates")
model = pickle.load(open('model.pkl', 'rb'))
model1 = pickle.load(open('model1.pkl','rb'))
@app.route('/')
def h():
    return render_template('h.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/index')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['GET'])
def predict():
    cgpa= request.args.get('cgpa')
    projects = request.args.get('projects')
    workshops = request.args.get('workshops')
    mini_projects = request.args.get('mini_projects')
    skills = request.args.get('skills')
    communication_skills = request.args.get('communication_skills')
    internship = request.args.get('internship')
    hackathon = request.args.get('hackathon')
    tw_percentage = request.args.get('tw_percentage')
    te_percentage = request.args.get('te_percentage')
    backlogs = request.args.get('backlogs')
    name=request.args.get('name')
    if cgpa=='':
        cgpa='0'
    if projects=='':
        projects='0'
    if workshops=='':
        workshops='0'
    if mini_projects=='':
        mini_projects='0'
    if communication_skills=='':
        communication_skills="0"
    if tw_percentage=='':
        tw_percentage='0'
    if te_percentage=='':
        te_percentage='0'
    if backlogs=='':
        backlogs='0'
    s=1
    for i in skills:
        if i==',':
            s=s+1
    
    arr = np.array([cgpa,projects,workshops,mini_projects,s,communication_skills,internship,hackathon,tw_percentage,te_percentage,backlogs])
    brr = np.asarray(arr,dtype=float)
    output = model.predict([brr])
    p=''
    if output=='Placed':
        p='1'
    else:
        p='0'
    arr1=np.array([cgpa,projects,workshops,mini_projects,s,communication_skills,internship,hackathon,tw_percentage,te_percentage,backlogs,p])
    brr1=np.asarray(arr1,dtype=float)
    salary=model1.predict([brr1])
    k=str(salary[0])
    l=0
    for i in k:
        l=l+1
    if l==6:
        k=k[0]+','+k[1]+k[2]+','+k[3]+k[4]+k[5]
    elif l==7:
        k=k[0]+k[1]+','+k[2]+k[3]+','+k[4]+k[5]+k[6]
    if(output=='Placed'):
        out = f'Congratualations {name} !! You have high chances of getting placed!!!'
        out2= f'Your Excepted Salary will be INR {k} per annum'
        return render_template('out.html', output=out,output2=out2)
    else:
        out=f'Sorry {name} !! You have low chances of getting placed.All the best!!!!'
        out2='Improve your skills...'
        return render_template('out.html', output=out,output2=out2)
     

if __name__ == "__main__":
    app.run(debug=True)