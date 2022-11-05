"""Основной файл для запуска сервиса."""
from flask import Flask, request
import classifier as clf
import transform
import json

app = Flask(__name__)


@app.route("/")
def index():
    return json.dumps({
        'message': "main API-page"
    })


@app.route("/classification", methods=['GET'])
def predict_class_and_probability():
    planned = request.args.get('planned', type=int)
    duration = request.args.get('duration', type=int)
    studio = request.args.get('studio', type=str)
    year = request.args.get('year', default=transform.CURRENT_YEAR, type=int)
    return clf.classify(planned, duration, studio, year)


if __name__ == '__main__':
    app.run(debug=True)
