from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/time_remaining")
def calculate_time():
    date_format = "%Y-%m-%d %H:%M:%S"

    target_time: datetime = datetime.strptime(request.args.get('target_time'), date_format)
    current_time: datetime = datetime.now()
    time_difference: timedelta = calculate_time_diff(current_time, target_time)
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    data = {
        "days": days,
        "hours": hours,
        "minutes": minutes
    }
    return jsonify(data)


def calculate_time_diff(start_time: datetime, target_time: datetime) -> timedelta:
    time_difference: timedelta = target_time - start_time
    return time_difference


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
