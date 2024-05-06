from flask import Flask, render_template, request
from login import login
from sensors import sensor
from actuators import actuators

app= Flask(__name__)

app.register_blueprint(login, url_prefix='/')
@app.route('/')
def index():
    return render_template('login.html')

app.register_blueprint(sensor, url_prefix='/')
@app.route('/sensors')
def sensors():
    return render_template("sensors.html")

app.register_blueprint(actuators, url_prefix='/')
@app.route('/actuators')
def actuator_list():
    return render_template("actuator.html")

@app.route('/home')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
