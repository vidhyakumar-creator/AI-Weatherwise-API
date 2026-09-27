from flask import Flask, render_template, request
from services.weather_service import get_weather
from services.ai_service import get_ai_advice

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    advice = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        try:
            weather = get_weather(city)
            advice = get_ai_advice(weather)
        except Exception as e:
            error = "Could not connect to the weather service"

    return render_template(
        "index.html",
        weather=weather,
        advice=advice,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
