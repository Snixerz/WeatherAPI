from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/weather')
def weather():
    return render_template('weather_form.html')

@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')

    params = {
        'q': users_city,
        'appid':"2608f679d4594364525f6c6cc2246c79"
    }
    response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=params)

    response_json = response.json()
    results = response_json.get('main').get('temp')
    return render_template('weather_results.html', results=results)