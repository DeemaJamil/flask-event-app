from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
from forms import EventForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'htux_python_course'

db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Event {self.title}, {self.date_posted}"


@app.route('/')
@app.route('/home')
def home():
    events = Event.query.all()
    return render_template('home.html', events=events)


@app.route('/create-event', methods=['GET', 'POST'])
def create_event():
    form = EventForm()

    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data
        )

        db.session.add(event)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('Create_event.html', form=form)


@app.route('/event-details/<int:eventId>')
def event_details(eventId):
    event = Event.query.get_or_404(eventId)
    return render_template('eventDetails.html', event=event)


if __name__ == '__main__':
    app.run(debug=True)