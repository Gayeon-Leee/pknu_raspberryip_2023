from flask import Flask, request,  render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT, initial=GPIO.HIGH)

@app.route("/")
def home():
    return render_template("button.html")

@app.route("/led/on")
def led_on():
    try:
        GPIO.output(ledPin, GPIO.LOW)
        return "ok"
    except expression as identifier:
        return "fail"


@app.route("/led/off")
def led_off():
    try:
        GPIO.output(ledPin, GPIO.HIGH)
        return "ok"
    except expression as identifier:
        return "fail"


if __name__ == "__main__":
        app.run(host='0.0.0.0', port='1122', debug=True)
