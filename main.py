from flask import Flask , render_template, request
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "app.db"))


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = "Who is Who in Myanmar"
db = SQLAlchemy(app)



@app.route('/',methods=['POST','GET'])
def home():
	people = BusinessLeader.query.all()
	return render_template("businessman.html",people=people)

@app.route('/businessman.html',methods=['POST','GET'])
def businessman():
	people = BusinessLeader.query.all()
	return render_template("businessman.html",people=people)


@app.route('/celebrity.html',methods=['POST','GET'])
def cele():
	people = Celebrity.query.all()
	return render_template("celebrity.html",people=people)

@app.route('/director.html',methods=['POST','GET'])
def director():
	people = Director.query.all()
	return render_template("director.html",people=people)

@app.route('/vocalist.html',methods=['POST','GET'])
def vocalist():
	people = Vocalist.query.all()
	return render_template("vocalist.html",people=people)

@app.route('/model.html',methods=['POST','GET'])
def model():
	people = Model.query.all()
	return render_template("model.html",people=people)

@app.route('/person/<link>')
def person(link):
        
        person = People.query.filter_by(link=link).first_or_404()
        return render_template("person.html",person=person)

class Vocalist(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(Politician,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<Politician %r>' % self.name

class BusinessLeader(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(BusinessLeader,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<BusinessLeader %r>' % self.name

class Model(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(BusinessLeader,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<BusinessLeader %r>' % self.name

class Celebrity(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(Celebrity,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<Celebrity %r>' % self.name

class Director(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(Celebrity,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<Celebrity %r>' % self.name

class People(db.Model):

	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(30),nullable=False)
	link=db.Column(db.String(10),nullable=False)
	occupation = db.Column(db.String(30),nullable=False)
	image = db.Column(db.Text,nullable=False)
	bio = db.Column(db.Text,nullable=True)

	def __init__(self,*args,**kwargs):
		super(People,self).__init__(*args,**kwargs)

	def __repr__(self):
		return '<People %r>' % self.name

if __name__ == '__main__':
    app.run(debug=True)
