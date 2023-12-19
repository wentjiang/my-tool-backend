from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time_remaining")
def calculate_time():
    date_format = "%Y-%m-%d %H:%M:%S"

    target_time = datetime.strptime(request.args.get('target_time'), date_format)
    print(target_time)
    current_time = datetime.now()
    time_difference = calculate_time_diff(current_time, target_time)
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds // 60) % 60
    data = {
        "hours": hours,
        "minutes": minutes
    }
    return jsonify(data)


def calculate_time_diff(start_time, target_time):
    time_difference = target_time - start_time
    return time_difference


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
