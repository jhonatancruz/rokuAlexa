import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import os

app= Flask(__name__)
ask= Ask(app, "/")


@ask.intent("OffIntent")
def off_tv():
    turnoff="curl -d ' ' http://10.30.39.192:8060/keypress/Poweroff"
    os.system(turnoff)
    turningoff= "Turning off"
    return statement(turningoff)

@ask.intent("OnIntent")
def on_tv():
    turnon= "curl -d ' ' http://10.30.39.192:8060/keypress/Poweron"
    os.system(turnon)
    turningon= "Turning on"
    return statement(turningon)

@ask.intent("NetflixIntent")
def netflix():
    netflix= "curl -d ' ' http://10.30.39.192:8060/launch/12?contentID=12"
    os.system(netflix)
    netflixing= "Okay! Have fun netflix and chilling!"
    return statement(netflixing)

@ask.intent("HomeIntent")
def tvhome():
    home= "curl -d ' ' http://10.30.39.192:8060/keypress/home"
    os.system(home)
    homing= "Home Sweet Home, okay!"
    return statement(homing)


if __name__ == '__main__':
    app.run(debug=True)
