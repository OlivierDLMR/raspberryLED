from flask import Flask, render_template, redirect, url_for, request
from led import Led
import RPi.GPIO as GPIO
from threading import Thread
app = Flask(__name__)

#Utilisation d'une norme de nommage pour les broches
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLed = Led(14)
greenLed = Led(15)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/on/<color>')
def on(color):
    if color == "red":
        redLed.on()
    elif color == "green":
        greenLed.on()
    return redirect(url_for('home'))

@app.route('/off/<color>')
def off(color):
    if color == "red":
        redLed.off()
        redLed.cancel()
    elif color == "green":
        greenLed.off()
        greenLed.cancel()
    return redirect(url_for('home'))

@app.route('/blink', methods=['POST'])
def blink():
    color = request.form['color']
    numBlink = int(request.form['numBlink'])
    sleepTime = float(request.form['sleepTime'])
    led = None
    if color == "red":
        led = redLed
    elif color == "green":
        led = greenLed
    thread = Thread(target=led.blink, args=(numBlink, sleepTime, ))
    thread.start()
    return redirect(url_for('home'))