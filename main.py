# main.py
from flask import Flask, render_template,  validate_on_submit , url_for , redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_wtf import FlaskForm
from forms import EventForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'htux_python_course'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Event {self.title}, {self.date_posted}"


@app.route('/about_us')
def about_us():
    return render_template('about_us.html')
@app.route('/home')
def home():
    events = Event.query.all()
    return render_template('home.html',events=events)

@app.route('/CreateEvent',methods=['GET','POST'])
def CreateEvent() :
   form = EventForm()
   if form.validate_on_submit() :
       event = Event()
       event.title = form.title.data
       event.description = form.description.data
       db.session.add(event)
       db.session.commit()

       return redirect(url_for('home'))
   return render_template('Create_event.html',form=form)

@app.route('/eventDetails/<int:eventId>')
def eventDetails(eventId):
     event = Event.query.get_or_404(eventId)
     return render_template('eventDetails.html',event=event)

if __name__ == '__main__' :

     app.run(debug=True)