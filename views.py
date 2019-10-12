from flask import Flask, render_template, request, redirect
from gpiozero import LED

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', **locals())

@app.route("/<action>/") 
def action(action):
    if action == "on":
        led.on() #Turn on  the led
        return redirect("/") #Redirect to the index page
    elif action == "off":
        led.off() #Turn off the led
        return redirect("/") #Redirect to the index page
    else:
        return redirect("/") #Redirect to the index page


if __name__ == "__main__":
    led = LED(17) #The led 17
    app.run(host='0.0.0.0')