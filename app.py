from flask import Flask, render_template, request
from weather import get_weather
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            weather = get_weather(city)

    current_time = datetime.now().strftime("%A, %d %B %Y")
    current_clock = datetime.now().strftime("%I:%M %p")

    return render_template(
        "index.html",
        weather=weather,
        date=current_time,
        time=current_clock
    )


if __name__ == "__main__":
    app.run(debug=True)