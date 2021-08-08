from flask import Flask, render_template, request, redirect, send_file, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime,date
# here we set all app configs
# aqui configuramos o app

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://xhvtplqn:ESYFvQFVgh8m1YLRbT4MZ_c3DqrD_S5b@tuffi.db.elephantsql.com/xhvtplqn'
db = SQLAlchemy(app)
app.secret_key ="123456"
# here we create a class for pet object
# aqui nós criamos uma classe para o objeto pet
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    breed = db.Column(db.String(50), nullable=False)
    food = db.Column(db.String(150), nullable=False)
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
#
# here we define the index route
# aqui definimos a rota do index
@app.route('/')
def index(): 
    session['user'] = None
    return render_template('index.html')
# here we define the home route
# aqui definimos a rota da pagina inicial
@app.route('/home')
def home(): 
    return render_template('views/home.html')
# here we define the profile route
# aqui definimos a rota do perfil do usuário
@app.route('/profile')
def profile(): 
    newlogin = User.query.get(session['user'])
    return render_template('views/profile.html',usersession = newlogin)
# importa pagina principal
# import home page
@app.route('/registeruser')
def registeruser():
    return render_template('registeruser.html')
# here we define the route for register pet
# aqui definimos a rota para o registro do animal de estimação
@app.route('/registerpet')
def registerpet():
    return render_template('registerpet.html')
# here we define he route for register pet script
# aqui nós definimos a rota para o script de registro de animais de estimação
@app.route('/registerusermessage',methods=['GET','POST'])
def newuser():
    message = ""
    if request.method == "POST":
        if request.form.get('input_password') == request.form.get('input_password_repeat'):
            newUser = User()
            newUser.name = str(request.form.get('input_name'))
            newUser.birthday = request.form.get('input_birthday')
            newUser.identity_number = int(request.form.get('input_identity_number'))
            newUser.email = str(request.form.get('input_email'))
            newUser.password = str(request.form.get('input_password'))
            insert(newUser)
    return render_template('response/sucess.html',message = "You are our new user!")
# here we define a route to page where shows a message about user registration
# aqui nos definimos a rota para a pagina de mensagem sobre o registro de usuário
@app.route('/registerpetmessage',methods=['GET','POST'])
def newpet():
    return redirect('/perfiluser')
# here we define a route to page where shows a message about pet registration
# aqui nos definimos a rota para a pagina de mensagem sobre o registro animais de estimação
@app.route('/jobs')
def jobs():
    return render_template('views/jobs.html')
# here we define a route for the login page
# aqui nós definimos uma rota para a pagina de login
@app.route('/login',methods=['GET','POST'])
def login():
    email =str(request.form.get('input_email'))

    newlogin = User.query.all()

    for i in newlogin:
            if i.password == str(request.form.get('input_password')) and i.email == email:
                session['user']=i.id 
                app.secret_key = i.password
                return render_template('response/sucess.html',message = "you are loging!")
# here we define a route for logout user
# aqui nós definimos uma rota para deslogar o usuário
@app.route('/loginout')
def loginout():
    session['user'] = None
    return redirect('/home')
# here we define a route for the update user values
# aqui nós definimos uma rota para atualizar os valores do usuário
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
    return render_template('response/sucess.html',message = "sucess!")
# here we send delete request
# aqui nós enviamos o pedido de esclusão ao banco
def delete(value,message = "sucess!"):
    db.session.delete(value)
    db.session.commit()
    return render_template('response/sucess.html',message = message)
# here we send update request
# aqui enviamos o pedido de atualização dos dados
def update(message = "sucess!"):
    db.session.commit()
    return render_template('response/sucess.html',message = message)
# here we add a new datavalue
# aqui nós adicionamos um novo valor no banco
def insert(value):
    db.session.add(value)
    db.session.commit()

    

if __name__ == '__main__':   
    db.create_all()
    app.run(debug=True)