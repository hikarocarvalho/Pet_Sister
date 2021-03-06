import os
from flask import Flask, render_template, request, redirect, send_file, url_for, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime,date
# here we set all app configs
# aqui configuramos o app
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/siter'
db = SQLAlchemy(app)
app.secret_key ="123456"
# here we create a class for pet object
# aqui nós criamos uma classe para o objeto pet
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    size = db.Column(db.Float, nullable=False)
    photopet = db.Column(db.Integer, nullable=True)
    medication = db.Column(db.String(150), nullable=True)
    petowner_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    # def __init__(self,name="",age=0,color="",weight=0,breed="",food="",medication=""):
    #     self.name = name
    #     self.age = age
    #     self.color = color
    #     self.weight = weight
    #     self.breed = breed
    #     self.food = food
    #     self.medication = medication
# here we create a class for users
# aqui nós criamos uma classe para os usuários
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=True)
    street = db.Column(db.String(50), nullable=True)
    block = db.Column(db.String(50), nullable=True)
    batch = db.Column(db.String(50), nullable=True)
    identity_number = db.Column(db.Integer, nullable=False)
    post_code = db.Column(db.Integer, nullable=True)
    address_other = db.Column(db.String(100), nullable=True)
    qualification = db.Column(db.String(100), nullable=True)
    recomendation = db.Column(db.String(100), nullable=True)
    pet = db.relationship('Pet', backref='user', lazy=True)
    job = db.relationship('Job', backref='pet', lazy=True)
    # def __init__(self,email="",password="",name="",birthday=datetime.now(),street="",block="",batch="",identity_number=0,post_code=0,address_other="",qualification="",recomendation=""):
    #     self.email=email
    #     self.password=password
    #     self.name = name
    #     self.birthday = birthday
    #     self.street = street
    #     self.block = block
    #     self.batch = batch
    #     self.identity_number = identity_number
    #     self.post_code = post_code
    #     self.address_other = address_other
    #     self.qualification = qualification
    #     self.recomendation = recomendation
# here we create a class for jobs
# aqui nos criamos uma classe para trabalhos
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(50), nullable=False)
    jobdateinit = db.Column(db.Date, nullable=True)
    jobdatefin = db.Column(db.Date, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
# here we define the index route
# aqui definimos a rota do index
@app.route('/')
def index(): 
    try:
        if session['user'] != None:
            return render_template('index.html',status=1)
        else:
            return render_template('index.html',status=0)
    except:
        session['user'] = None
        return render_template('index.html',status=0)
# here we define the home route
# aqui definimos a rota da pagina inicial
@app.route('/home')
def home(): 
    return render_template('views/home.html')
# here we define the profile route
# aqui definimos a rota do perfil do usuário
@app.route('/profile')
def profile(): 
    try:
        if session['user'] != None:
            newlogin = User.query.get(session['user'])
            pets = getAllPets()
            return render_template('views/profile.html',usersession = newlogin,pets = pets)
        else:
            return redirect('/home')
    except:
        session['user'] = None
        return redirect('/home')
# here is defined the profile route for the pet
# aqui está definido a rota do perfil do animal de estimação
@app.route('/profilepet/<id>')
def profilepet(id): 
    try:
        if session['user'] != None:
            idpet = id
            newlogin = User.query.get(session['user'])
            pet = Pet.query.get(idpet)
            return render_template('views/profilepet.html',pet = pet)
        else:
            return redirect('/home')
    except:
        session['user'] = None
        return redirect('/home')
# importa pagina principal
# import home page
@app.route('/jobs')
def jobs():
    try:
        if session['user'] != None:
            newlogin = User.query.get(session['user'])
            jobs = getAllJobs()
            return render_template('views/jobs.html',jobs = jobs)
        else:
            return redirect('/home')
    except:
        session['user'] = None
        return redirect('/home')
@app.route('/registeruser')
def registeruser():
    return render_template('registers/user.html')
# here we define the route for register pet
# aqui definimos a rota para o registro do animal de estimação
@app.route('/registerpet')
def registerpet():
    return render_template('registers/pet.html')
@app.route('/newjob')
def registerjob():
    return render_template('registers/newjob.html')
# here we define he route for register pet script
# aqui nós definimos a rota para o script de registro de animais de estimação
@app.route('/registerusermessage',methods=['GET','POST'])
def newuser():
    message = ""
    location = "/profile"
    if request.method == "POST":
        if request.form.get('input_password') == request.form.get('input_password_repeat'):
            newUser = User()
            newUser.name = str(request.form.get('input_name'))
            newUser.birthday = request.form.get('input_birthday')
            newUser.identity_number = int(request.form.get('input_identity_number'))
            newUser.email = str(request.form.get('input_email'))
            newUser.password = str(request.form.get('input_password'))
            if insert(newUser):
                loged(newUser.email, newUser.password)
                location = "/profile"
                message = "You are our new user!"
            else:
                message = "Existing Account"
                location = "/registeruser"
    
    return render_template('response/sucess.html',message = message,location=location)
# here we define a route to page where shows a message about user registration
# aqui nos definimos a rota para a pagina de mensagem sobre o registro de usuário
@app.route('/registerpetmessage',methods=['GET','POST'])
def newpet():
    message = ""
    location = "/profile"
    if request.method == "POST":
        if request.form.get('input_password') == request.form.get('input_password_repeat'):
            newPet = Pet()
            newPet.name = str(request.form.get('input_name'))
            newPet.age = request.form.get('input_age')
            newPet.weight = float(request.form.get('input_weight'))
            newPet.size = float(request.form.get('input_size'))
            newPet.medication = str(request.form.get('input_medicine'))
            newPet.petowner_id = session['user']
            newPet.photopet = request.form.get('animal')
            db.session.add(newPet)
            db.session.commit()
            message = "You have a new pet!"
    
    return render_template('response/sucess.html',message = message,location=location)
# here we define a route to page where shows a message about job registration
# aqui nos definimos a rota para a pagina de mensagem sobre o registro de trabalhos
@app.route('/registerjobmessage',methods=['GET','POST'])
def newjob():
    message = ""
    location = "/jobs"
    if request.method == "POST":
        newjob = Job()
        newjob.description = str(request.form.get('input_description'))
        newjob.jobdateinit = request.form.get('input_dateinit')
        newjob.jobdatefin = request.form.get('input_datefin')
        newjob.user_id = session['user']
        db.session.add(newjob)
        db.session.commit()
        message = "You now have one job for others!"
    
    return render_template('response/sucess.html',message = message,location=location)
# here we define a route for the login page
# aqui nós definimos uma rota para a pagina de login
@app.route('/login',methods=['GET','POST'])
def login():
    email =str(request.form.get('input_email'))
    password = str(request.form.get('input_password'))
    message = ""
    if loged(email, password):
        message = "you are loging!"
        return render_template('response/sucess.html',message = message,location="/profile")
    else:
        message ="Error Account"
        return render_template('response/sucess.html',message = message,location="/home")       
# here we define a route for logout user
# aqui nós definimos uma rota para deslogar o usuário
@app.route('/loginout')
def loginout():
    session['user'] = None
    return render_template('response/sucess.html',message = "You has been login out, sucess!",location="/home")
# here we define a route for the update user values
# aqui nós definimos uma rota para atualizar os valores do usuário
@app.route('/updatepet/<id>',methods=['GET','POST'])
def updatepet(id):
    newupdate = Pet.query.get(id)
    newupdate.name = str(request.form.get('input_name'))
    newupdate.age = request.form.get('input_age')
    newupdate.weight = float(request.form.get('input_weight'))
    newupdate.size = float(request.form.get('input_size'))
    newupdate.medication = str(request.form.get('input_medicine'))
    newupdate.photopet = request.form.get('animal')
    update("sucess!")
    return render_template('response/sucess.html',message = "sucess!",location="/profile")
@app.route('/updateuser',methods=['GET','POST'])
def updateuser():
    newupdate = User.query.get(session['user'])
    newupdate.email = request.form.get('input_email')
    newupdate.password = request.form.get('input_password')
    newupdate.name = request.form.get('input_name')
    newupdate.birthday = request.form.get('input_birthday')
    newupdate.street = request.form.get('input_street')
    newupdate.block = request.form.get('input_block')
    newupdate.batch = request.form.get('input_batch')
    newupdate.identity_number = request.form.get('input_identity_number')
    newupdate.post_code = request.form.get('input_post_code')
    newupdate.address_other = request.form.get('input_address_other')
    newupdate.qualification = request.form.get('input_qualification')
    newupdate.recomendation = request.form.get('input_recomandation')
    update("sucess!")
    return render_template('response/sucess.html',message = "sucess!",location="/profile")
# here we define a route to remove a user from database
# aqui nós definimos uma rota para remover um usuário da base de dados
@app.route('/remove/<id>')
def remove(id):
    userRemove = User.query.get(id)
    session['user'] = None
    delete(userRemove)
    return render_template('response/sucess.html',message = "user has been deleted",location="/home")
@app.route('/removepet/<id>')
def removepet(id):
    petRemove = Pet.query.get(id)
    delete(petRemove)
    return render_template('response/sucess.html',message = "Your pet has been deleted",location="/home")
# here we setup loged user
# aqui setamos o usuário logado
def loged(email,password):
    newlogin = User.query.all()
    for i in newlogin:
        if i.password == password and i.email == email:
            session['user']=i.id 
            app.secret_key = i.password
            return True
    return False
# here we send delete request
# aqui nós enviamos o pedido de esclusão ao banco
def delete(value):
    db.session.delete(value)
    db.session.commit()
    return True
# here we send update request
# aqui enviamos o pedido de atualização dos dados
def update(message = "sucess!"):
    db.session.commit()
    return render_template('response/sucess.html',message = message)
# here we add a new datavalue
# aqui nós adicionamos um novo valor no banco
def insert(value):
    users = User.query.all()
    for i in users:
        if i.email == value.email:
            return False
    db.session.add(value)
    db.session.commit()
    return True
# get all pet from user
# pega todos os petes do usuário
def getAllPets():
    session['user'] 
    pets = userRemove = Pet.query.filter_by(petowner_id=session['user'])
    return pets
#get all jobs 
#pega todos trabalhos
def getAllJobs():
    session['user'] 
    jobs = userRemove = Job.query.all()
    return jobs
def getAllPetsByJob(value):
    session['user']
    petdict = dict()
    for i.pet_id in value:
        petdict[i] = Pet.query.filter_by(id=i).photopet
    return petdict
# get photo and save
# pega a foto e salva
def photoPet(file):
        # if user does not select file, browser also
        # submit a empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    else:
        filename = secure_filename(file.filename)
        file.save(os.path.join("/static/img/photospet", filename))
# the function here start de app 
# aqui a função inicia o aplicativo
if __name__ == '__main__':  
    db.create_all()
    app.run(debug=True)