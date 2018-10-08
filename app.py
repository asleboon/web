from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, AnyOf
from flask_login import LoginManager



app = Flask(__name__)
Bootstrap(app)
login_manager = LoginManager(app)
app.config["SECRET_KEY"] = "mysecret"

class LoginForm(Form):
    username = StringField('username', validators=[InputRequired(), Email(message="Wrong username or password")])
    password = PasswordField('password', validators=[InputRequired(), Length(min=5, max=20), AnyOf([])])

@app.route('/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return "Success"
    return render_template("index.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)