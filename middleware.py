from flask import jsonify
from flask import request
import sys
from datetime import datetime, timedelta
import tzlocal


def hello():
    return "<h1 style='color:teal'>Hello from Python Flask</h1>"


def hello2():
    return jsonify({"msg": "Hello from Python"})


def bye2():
    return jsonify({"msg": "Goodbye from Python"})


def bye():
    return "<h1 style='color:deeppink'>Goodbye from Python Flask</h1>"


def message():
    return "<h1 style='color:darkmagenta'>Welcome</h1><p>This is a simple api method that returns some HTML</p>" \
           "<p>Some methods return HTML, others return data as JSON</p>"


def version():
    return "<h1 style='color:grey'>Python Version Information</h1><h3>" + sys.version + "</h3>"


def list_methods(app):
    output1 = "<h1>Routes for this api</h1><ul>"
    output2 = ""
    routes = []

    for rt in app.url_map.iter_rules():
        routes.append(str(rt))

    routes.sort()

    for rt in routes:
        output2 = output2 + '<li>IP Address:5000' + str(rt) + '</li>'

    output3 = "</ul>"
    return output1 + output2 + output3


def list_methods2(app):
    result = []
    routes = []

    for rt in app.url_map.iter_rules():
        routes.append(str(rt))

    routes.sort()

    for rt in routes:
        result.append('IP Address:5000' + str(rt))

    return jsonify({"Routes": result})


def localtime():
    a = now()
    dt_string = a.strftime("%d/%m/%Y %H:%M:%S%z")
    return "<h3 style='color:maroon'>Local Data and Time</h3><p>" + dt_string + "</p>"


def localtime2():
    a = now()
    dt_string = a.strftime("%d/%m/%Y %H:%M:%S%z")
    return jsonify({"msg": "Local Data and Time is " + dt_string})


def add_hours_to_localtime():
    num_hours = request.form["num_hours"]
    a = now() + timedelta(hours=float(num_hours))
    dt_string = a.strftime("%d/%m/%Y %H:%M:%S%z")
    return "<h3 style='color:darkgreen'>Local Data and Time with " + str(num_hours) + " Hour(s) Added</h3><p>" + dt_string + "</p>"


def add_hours_to_localtime2():
    num_hours = request.form["num_hours"]
    a = now() + timedelta(hours=float(num_hours))
    dt_string = a.strftime("%d/%m/%Y %H:%M:%S%z")
    return jsonify({'hours_added': num_hours, 'futuretime': dt_string})


# time helper function
def now():
    return tzlocal.get_localzone().localize(datetime.now())
